to export gui: pyuic6 -x "D:\Documents\```GitHub\CIST 1620\PROJECT\project-calculator\calculator_gui.ui" -o "D:\Documents\```GitHub\CIST 1620\PROJECT\project-calculator\gui.py"
to export gui images: pyside6-rcc "D:\Documents\```GitHub\CIST 1620\PROJECT\project-calculator\graphics\resources.qrc" -o "D:\Documents\```GitHub\CIST 1620\PROJECT\project-calculator\graphics\resources.py"
	need to change line to: from PyQt6 import QtCore

may want to consider requiring a pin to make a deposit/withdrawal for the first time on login?