# NexGenLogGuide
This project was done to parse the log files. The Gui was developed using PYQT5

Folder Structure:
=================
misc
    |--> contains generated files for reference, it has no action to look in to.
res
    |
    |--> about.jpg
    |--> index.png

ui_files
    |
    |--> NextGenLogGuide.ui - Main window GUI part (files generated using QT Creator )
    |--> GccGraph.ui        - Graph Gui part
    |--> about.ui           - About dialog gui part
    |--> To generate python file use "pyuic5.exe -o Filename.ui Filename.py "


NextGenLogGuide.py      - Main file which triggers the execution
NextGenLogGuideGui.py   - All Gui related operations are implemented here.
GccGraph.py             - Full Gcc graph implementation are here.
about.py                - About dialog for this software.
setup_logger.py         - python Logger 
utils.py                - Contains util functionalities for the NextGenLogGuide  

LogConfig.json          - Config file for the NextGenLogGuide
NextGenLogGuideGui.exe  - This is generated using pyinstaller, Command used "pyinstaller.exe --onefile  NextGenLogGuide.py"
