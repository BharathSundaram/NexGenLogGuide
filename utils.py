
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QObject, pyqtSignal, pyqtSlot, QRunnable
from setup_logger import logger
import os

__filename__ = "utils.py"

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
            return 1, Oneliner,Settings
    except:
        return 0 , [], []       
