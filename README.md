# NexGenLogGuide
This project was done to parse the log files. The Gui was developed using PYQT5

Folder Structure:
=================
res
    |
    |-----> about.jpg
    |-----> index.png

ui_files
    |
    |-----> NextGenLogGuide.ui --- Ui files generated using QT Creator 

NextGenLogGuide.py --- Main file which triggers the execution
NextGenLogGuideGui.py --- All Gui related operations are implemented here.
setup_logger.py --- python Logger 
utils.py --- Contains util functionalities for the NextGenLogGuide  
LogConfig.json --- Config file for the NextGenLogGuide
NextGenLogGuideGui.exe --- This is geneared using pyinstaller, Command used "pyinstaller.exe --onefile -w   NextGenLogGuide.py"
