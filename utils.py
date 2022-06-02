
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QObject, pyqtSignal, pyqtSlot, QRunnable
from setup_logger import logger
import os,sys,json,time,re,traceback

__filename__ = "utils.py"
__author__ = "Bharath Shanmugasundaram"


def get_screen_resolution():
    screen_resolution = QtWidgets.QDesktopWidget().screenGeometry()
    return (screen_resolution.width(), screen_resolution.height())

def get_files_from_dir(path,fext):
    file_list = []    
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(fext):
                fpath = os.path.join(root, file)
                logger.info(fpath)
                file_list.append(fpath)
    return file_list

class WorkerSignals(QObject):
    finished = pyqtSignal()
    send_data = pyqtSignal(tuple)
    error = pyqtSignal(tuple)

class JobThread(QRunnable):
    def __init__(self,fn,file_list):
        super(JobThread, self).__init__()
        self.fn = fn
        self.file_list = file_list
        self.is_paused = False
        self.is_killed = False
        self.signals = WorkerSignals()
        logger.info(self)
        
    @pyqtSlot()
    def run(self):
        try:
            self.isalive = True    
            self.fn(self.file_list, self.signals.send_data)
        except:
            #traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            pass
        finally:
            self.signals.finished.emit()  # Done
            


def ReadConfigfromJson(filename):
    try:
        with open(filename) as data_file:
            Oneliner = []
            Settings = []
            FullGcc  = []
            data = json.load(data_file)
            for item in data['Oneliner']:
                temp = [item]
                logger.info(__filename__,temp)
                Oneliner.append(temp)
            for item in data['Setting']:
                temp = [item]
                logger.info(__filename__,temp)
                Settings.append(temp)
            for item in data['FullGC']:
                temp = [item]
                logger.info(__filename__,temp)
                FullGcc.append(temp)
            return True, Oneliner,Settings,FullGcc
    except NameError as nameerror:
        logger.info(__filename__ , "Unexpected error:", nameerror)
        return False , [], [], []

def get_regex_from_list(jsonlist):
    regex_str=''
    count = 0
    for line in jsonlist:
        print(line[0]['Regex'])
        regex_str = regex_str + '|' + line[0]['Regex']
        count = count + 1
    # Slice string to remove first character
    regex_str = regex_str[1 : : ]
    logger.info(__filename__,regex_str)
    return count,regex_str

def extract_onliner_info(regex_count,regex_str,filename):

    #seconds = time.time()
    #logger.info(__filename__,'Time taken:',seconds)	
    regex=re.compile(regex_str,re.I)
    lines=[]
    with open(filename,errors='ignore') as filedata:
        count = 0
        while True: 
            line = filedata.readline() 
            if not line: 
                break
            if regex_count == 0:
                break

            count += 1
            match = re.search(regex,line)
            if match != None:
                logger.info(line)
                lines.append(line[:-1:])
                regex_count = regex_count - 1
    
    if(len(lines)>0): #if not lines it may be invalid file
        uptime = SearchUpTime(filename)
        if(len(uptime)==3):
            hour = int(uptime[0]/60)
            minute = uptime[0] % 60
            formatstr = str("Approx Box ran for {} Hours {} minutes {} seconds {} milliseconds ".format(hour,minute,\
                            uptime[1], uptime[2]))
            lines.append(formatstr)

    #seconds = time.time()
    #logger.info(__filename__,'Time taken:',seconds,'line parsed', count)
    return None if not lines else lines

def get_FullGcc_from_list(jsonlist):
    #jsonlist contains dict to loop through
    subjsonlist = jsonlist[0]
    gccRex =''
    gccMarker = ''
    for key,value in subjsonlist[0].items():
        if key =='Regex':
            gccRex = value
        elif key == 'Marker':
            gccMarker = value
    
    if(gccRex =='' or gccMarker == ''):
        return False ,[]
    else:
        return True, [gccRex,gccMarker]

def initglobals():
    global author, version, recent_file_size, recentFiles_name
    author = "Bharath Shanmugasundaram"
    version = "1.0.0"
    recentFiles_name = 'Recentfiles.txt'
    recent_file_size = 6
    


def get_version():
    return version

def get_author():
    return author

def get_recent_file_size():
    return recent_file_size

def get_recentFiles_name():
    return recentFiles_name


def writeRecentFilestoFile(filelist):
    filename = get_recentFiles_name()
    if(True == os.path.isfile(filename)):
        os.remove(filename)

    with open(filename,'w') as text_file:
        for fname in filelist:
            text_file.write(fname.text() + '\n')

def LoadRecentFilestoFile():
    filename = get_recentFiles_name()
    if(True != os.path.isfile(filename)):
        return []

    with open(get_recentFiles_name()) as text_file:
        filelist = []
        while True:
            fname = text_file.readline() 
            if not fname:
                break
            filelist.append(fname.rstrip(os.linesep))
    return filelist

def SearchUpTime(file_name):
    # Create an empty list to keep the track of last N lines
    timelist = []
    linecount = 0
    # Open file for reading in binary mode
    with open(file_name, 'rb') as read_obj:
        # Move the cursor to the end of the file
        read_obj.seek(0, os.SEEK_END)
        # Create a buffer to keep the last read line
        buffer = bytearray()
        # Get the current position of pointer i.e eof
        pointer_location = read_obj.tell()
        # Loop till pointer reaches the top of the file
        while pointer_location >= 0:
            # Move the file pointer to the location pointed by pointer_location
            read_obj.seek(pointer_location)
            # Shift pointer location by -1
            pointer_location = pointer_location -1
            # read that byte / character
            new_byte = read_obj.read(1)
            # If the read byte is new line character then it means one line is read
            if new_byte == b'\n':
                linecount = linecount + 1
                # Save the line in list of lines
                line = buffer.decode(errors='ignore')[::-1]
                timelist = extract_time_info(line)
                if len(timelist) > 0 and linecount > 150:
                    break
                # Reinitialize the byte array to save next line
                buffer = bytearray()
            else:
                # If last read character is not eol then add it in buffer
                buffer.extend(new_byte)

        '''May not happen is what we presume
        
        if len(buffer) > 0:
            line = buffer.decode()[::-1]'''
        return timelist

def extract_time_info(line):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    trace_levels = ['DEBUG', 'INFO', 'WARN' , 'ERROR']
    #check valid line
    #print(line.split(' '))
    spacesplitl =line.split(' ')
    if(len(spacesplitl) > 2):
        #print(spacesplitl[2])
        if(spacesplitl[2] not in trace_levels):
            return []
    timeval = spacesplitl[0].split(':')
    if 1 == len(timeval) and timeval[0] in days:
        del timeval
        line = spacesplitl[1]
        timeval = spacesplitl[0].split(':')

    if ( len(timeval) == 2
            and True == str(timeval[0]).isdigit()
            and True == str(timeval[1].split('.')[0]).isdigit()
            and True == str(timeval[1].split('.')[1]).isdigit()):
        minutes = int(timeval[0])
        seconds =int(timeval[1].split('.')[0])
        millseconds = int(timeval[1].split('.')[1])
        return [minutes,seconds,millseconds]
    else:
        return []

