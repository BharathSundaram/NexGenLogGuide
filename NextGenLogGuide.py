
from NextGenLogGuideGui import *
from setup_logger import logger

__filename__ = "NextGenLogGuide"
__author__ = "Bharath Shanmugasundaram"
__license__ = "GPL"
__email__ = "bharath.inmail@gmail.com"
__status__ = "Production"

ui= lambda: None
if __name__ == "__main__":
    import sys
    logger.debug(__filename__,"NexGenLogGuideStarted")
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    app.setWindowIcon(QIcon(scriptDir + os.path.sep + 'res' + os.path.sep + 'index.png'))
    ui.show()
    app.exec_()
