
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QObject, pyqtSignal, pyqtSlot, QRunnable
from setup_logger import logger
import os,sys,json,time,re


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
    error = pyqtSignal(tuple)

class JobThread(QRunnable):
    
    signals = WorkerSignals()
    
    def __init__(self,fn,file_list,log_info_list):
        super().__init__()
        self.fn = fn
        self.file_list = file_list
        self.log_info_list = log_info_list
        self.is_paused = False
        self.is_killed = False
        logger.info(self)
        
    @pyqtSlot()
    def run(self):
        try:
            self.fn(self.file_list, self.log_info_list)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        finally:
            self.signals.finished.emit()  # Done
            

    def pause(self):
        self.is_paused = True
        
    def resume(self):
        self.is_paused = False
        
    def kill(self):
        self.is_killed = True

def ReadConfigfromJson(filename):
    try:
        with open(filename) as data_file:
            Oneliner = []
            Settings = []
            data = json.load(data_file)
            for item in data['Oneliner']:
                temp = [item]
                logger.info(__filename__,temp)
                Oneliner.append(temp)
            for item in data['Setting']:
                temp = [item]
                logger.info(__filename__,temp)
                Settings.append(temp)
            return True, Oneliner,Settings
    except NameError as nameerror:
        logger.info(__filename__ , "Unexpected error:", nameerror)
        return False , [], []       

def get_regex_from_list(jsonlist):
    regex_str=''
    for line in jsonlist:
        print(line[0]['Regex'])
        regex_str = regex_str + '|' + line[0]['Regex']
    # Slice string to remove first character
    regex_str = regex_str[1 : : ]
    logger.info(__filename__,regex_str)
    return regex_str

def extract_onliner_info(regex_str,filename):

    seconds = time.time()
    logger.info(__filename__,'Time taken:',seconds)	
    regex=re.compile(regex_str,re.I)
    lines=[]
    with open(filename) as filedata:
        count = 0
        while True: 
            line = filedata.readline() 
            if not line: 
                break
            count += 1
            match = re.search(regex,line)
            if match != None:
                logger.info(line)
                lines.append(line[:-1:]) 

    seconds = time.time()
    logger.info(__filename__,'Time taken:',seconds,'line parsed', count)
    return None if not lines else lines
