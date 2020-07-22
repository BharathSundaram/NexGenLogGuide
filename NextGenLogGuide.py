from NextGenLogGuideGui import *
from setup_logger import logger
__filename__ = "NextGenLogGuide"

if __name__ == "__main__":
    import sys
    logger.debug(__filename__,"called")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.add_signals(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())