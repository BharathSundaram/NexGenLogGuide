
from PyQt5 import QtWidgets

def get_screen_resolution():
    screen_resolution = QtWidgets.QDesktopWidget().screenGeometry()
    return (screen_resolution.width(), screen_resolution.height())