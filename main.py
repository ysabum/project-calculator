from logic import *
import sys

def main():   
    application = QApplication([])
    window = Logic()
    window.setWindowTitle('Calculator')
    window.setWindowIcon(QtGui.QIcon(":/calculator/calculator.png"))
    window.show()
    application.exec()
    sys.exit()
    
if __name__ == '__main__':
    main()