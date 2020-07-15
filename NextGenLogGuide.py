from NextGenLogGuideGui import *
from setup_logger import logger

if __name__ == "__main__":
    import sys
    logger.debug(__name__,"called")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.add_signals()
    MainWindow.show()
    sys.exit(app.exec_())