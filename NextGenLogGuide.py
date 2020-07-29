
from NextGenLogGuideGui import *
from setup_logger import logger

__filename__ = "NextGenLogGuide"
__author__ = "Bharath Shanmugasundaram"
__license__ = "GPL"
__email__ = "bharath.inmail@gmail.com"
__status__ = "Production"

if __name__ == "__main__":
    import sys
    logger.debug(__filename__,"called")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.add_signals(MainWindow)
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    app.setWindowIcon(QIcon(scriptDir + os.path.sep + 'res' + os.path.sep + 'index.png'))
    MainWindow.show()
    sys.exit(app.exec_())
