# Form implementation generated from reading ui file 'D:\Documents\```GitHub\CIST 1620\PROJECT\project-calculator\calculator_gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(700, 650)
        Calculator.setMinimumSize(QtCore.QSize(350, 650))
        Calculator.setMaximumSize(QtCore.QSize(700, 650))
        self.calculator_screen = QtWidgets.QLineEdit(parent=Calculator)
        self.calculator_screen.setGeometry(QtCore.QRect(20, 20, 315, 131))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_screen.setFont(font)
        self.calculator_screen.setText("")
        self.calculator_screen.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.calculator_screen.setReadOnly(True)
        self.calculator_screen.setObjectName("calculator_screen")
        self.calculator_push7 = QtWidgets.QPushButton(parent=Calculator)
        self.calculator_push7.setGeometry(QtCore.QRect(20, 320, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_push7.setFont(font)
        self.calculator_push7.setStyleSheet("QPushButton{background-color: rgb(220, 220, 220); border: 1px solid gray;}\n"
"QPushButton:hover {background-color: rgb(198, 198, 198)}")
        self.calculator_push7.setCheckable(True)
        self.calculator_push7.setChecked(False)
        self.calculator_push7.setObjectName("calculator_push7")
        self.calculator_pushNumeric_buttonGroup = QtWidgets.QButtonGroup(Calculator)
        self.calculator_pushNumeric_buttonGroup.setObjectName("calculator_pushNumeric_buttonGroup")
        self.calculator_pushNumeric_buttonGroup.addButton(self.calculator_push7)
        self.calculator_push8 = QtWidgets.QPushButton(parent=Calculator)
        self.calculator_push8.setGeometry(QtCore.QRect(100, 320, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_push8.setFont(font)
        self.calculator_push8.setStyleSheet("QPushButton{background-color: rgb(220, 220, 220); border: 1px solid gray;}\n"
"QPushButton:hover {background-color: rgb(198, 198, 198)}")
        self.calculator_push8.setCheckable(True)
        self.calculator_push8.setChecked(False)
        self.calculator_push8.setObjectName("calculator_push8")
        self.calculator_pushNumeric_buttonGroup.addButton(self.calculator_push8)
        self.calculator_push9 = QtWidgets.QPushButton(parent=Calculator)
        self.calculator_push9.setGeometry(QtCore.QRect(180, 320, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_push9.setFont(font)
        self.calculator_push9.setStyleSheet("QPushButton{background-color: rgb(220, 220, 220); border: 1px solid gray;}\n"
"QPushButton:hover {background-color: rgb(198, 198, 198)}")
        self.calculator_push9.setCheckable(True)
        self.calculator_push9.setChecked(False)
        self.calculator_push9.setObjectName("calculator_push9")
        self.calculator_pushNumeric_buttonGroup.addButton(self.calculator_push9)
        self.calculator_push6 = QtWidgets.QPushButton(parent=Calculator)
        self.calculator_push6.setGeometry(QtCore.QRect(180, 400, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_push6.setFont(font)
        self.calculator_push6.setStyleSheet("QPushButton{background-color: rgb(220, 220, 220); border: 1px solid gray;}\n"
"QPushButton:hover {background-color: rgb(198, 198, 198)}")
        self.calculator_push6.setCheckable(True)
        self.calculator_push6.setChecked(False)
        self.calculator_push6.setObjectName("calculator_push6")
        self.calculator_pushNumeric_buttonGroup.addButton(self.calculator_push6)
        self.calculator_push4 = QtWidgets.QPushButton(parent=Calculator)
        self.calculator_push4.setGeometry(QtCore.QRect(20, 400, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_push4.setFont(font)
        self.calculator_push4.setStyleSheet("QPushButton{background-color: rgb(220, 220, 220); border: 1px solid gray;}\n"
"QPushButton:hover {background-color: rgb(198, 198, 198)}")
        self.calculator_push4.setCheckable(True)
        self.calculator_push4.setChecked(False)
        self.calculator_push4.setObjectName("calculator_push4")
        self.calculator_pushNumeric_buttonGroup.addButton(self.calculator_push4)
        self.calculator_push5 = QtWidgets.QPushButton(parent=Calculator)
        self.calculator_push5.setGeometry(QtCore.QRect(100, 400, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_push5.setFont(font)
        self.calculator_push5.setStyleSheet("QPushButton{background-color: rgb(220, 220, 220); border: 1px solid gray;}\n"
"QPushButton:hover {background-color: rgb(198, 198, 198)}")
        self.calculator_push5.setCheckable(True)
        self.calculator_push5.setChecked(False)
        self.calculator_push5.setObjectName("calculator_push5")
        self.calculator_pushNumeric_buttonGroup.addButton(self.calculator_push5)
        self.calculator_push3 = QtWidgets.QPushButton(parent=Calculator)
        self.calculator_push3.setGeometry(QtCore.QRect(180, 480, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_push3.setFont(font)
        self.calculator_push3.setStyleSheet("QPushButton{background-color: rgb(220, 220, 220); border: 1px solid gray;}\n"
"QPushButton:hover {background-color: rgb(198, 198, 198)}")
        self.calculator_push3.setCheckable(True)
        self.calculator_push3.setChecked(False)
        self.calculator_push3.setObjectName("calculator_push3")
        self.calculator_pushNumeric_buttonGroup.addButton(self.calculator_push3)
        self.calculator_push1 = QtWidgets.QPushButton(parent=Calculator)
        self.calculator_push1.setGeometry(QtCore.QRect(20, 480, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_push1.setFont(font)
        self.calculator_push1.setStyleSheet("QPushButton{background-color: rgb(220, 220, 220); border: 1px solid gray;}\n"
"QPushButton:hover {background-color: rgb(198, 198, 198)}")
        self.calculator_push1.setCheckable(True)
        self.calculator_push1.setChecked(False)
        self.calculator_push1.setObjectName("calculator_push1")
        self.calculator_pushNumeric_buttonGroup.addButton(self.calculator_push1)
        self.calculator_push2 = QtWidgets.QPushButton(parent=Calculator)
        self.calculator_push2.setGeometry(QtCore.QRect(100, 480, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_push2.setFont(font)
        self.calculator_push2.setStyleSheet("QPushButton{background-color: rgb(220, 220, 220); border: 1px solid gray;}\n"
"QPushButton:hover {background-color: rgb(198, 198, 198)}")
        self.calculator_push2.setCheckable(True)
        self.calculator_push2.setChecked(False)
        self.calculator_push2.setObjectName("calculator_push2")
        self.calculator_pushNumeric_buttonGroup.addButton(self.calculator_push2)
        self.calculator_pushTurnNegative = QtWidgets.QPushButton(parent=Calculator)
        self.calculator_pushTurnNegative.setGeometry(QtCore.QRect(20, 560, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_pushTurnNegative.setFont(font)
        self.calculator_pushTurnNegative.setStyleSheet("QPushButton{background-color: rgb(220, 220, 220); border: 1px solid gray;}\n"
"QPushButton:hover {background-color: rgb(198, 198, 198)}")
        self.calculator_pushTurnNegative.setCheckable(True)
        self.calculator_pushTurnNegative.setChecked(False)
        self.calculator_pushTurnNegative.setObjectName("calculator_pushTurnNegative")
        self.calculator_pushNumeric_buttonGroup.addButton(self.calculator_pushTurnNegative)
        self.calculator_push0 = QtWidgets.QPushButton(parent=Calculator)
        self.calculator_push0.setGeometry(QtCore.QRect(100, 560, 75, 75))
        self.calculator_push0.setMinimumSize(QtCore.QSize(0, 0))
        self.calculator_push0.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_push0.setFont(font)
        self.calculator_push0.setStyleSheet("QPushButton{background-color: rgb(220, 220, 220); border: 1px solid gray;}\n"
"QPushButton:hover {background-color: rgb(198, 198, 198)}")
        self.calculator_push0.setCheckable(True)
        self.calculator_push0.setChecked(False)
        self.calculator_push0.setObjectName("calculator_push0")
        self.calculator_pushNumeric_buttonGroup.addButton(self.calculator_push0)
        self.calculator_pushDecimal = QtWidgets.QPushButton(parent=Calculator)
        self.calculator_pushDecimal.setGeometry(QtCore.QRect(180, 559, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_pushDecimal.setFont(font)
        self.calculator_pushDecimal.setStyleSheet("QPushButton{background-color: rgb(220, 220, 220); border: 1px solid gray;}\n"
"QPushButton:hover {background-color: rgb(198, 198, 198)}")
        self.calculator_pushDecimal.setCheckable(True)
        self.calculator_pushDecimal.setChecked(False)
        self.calculator_pushDecimal.setObjectName("calculator_pushDecimal")
        self.calculator_pushNumeric_buttonGroup.addButton(self.calculator_pushDecimal)
        self.calculator_pushMultiply = QtWidgets.QPushButton(parent=Calculator)
        self.calculator_pushMultiply.setGeometry(QtCore.QRect(260, 320, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_pushMultiply.setFont(font)
        self.calculator_pushMultiply.setStyleSheet("QPushButton{background-color: rgb(220, 220, 220); border: 1px solid gray;}\n"
"QPushButton:hover {background-color: rgb(198, 198, 198)}")
        self.calculator_pushMultiply.setCheckable(True)
        self.calculator_pushMultiply.setChecked(False)
        self.calculator_pushMultiply.setObjectName("calculator_pushMultiply")
        self.calculator_operator_buttonGroup = QtWidgets.QButtonGroup(Calculator)
        self.calculator_operator_buttonGroup.setObjectName("calculator_operator_buttonGroup")
        self.calculator_operator_buttonGroup.addButton(self.calculator_pushMultiply)
        self.calculator_pushCalculate = QtWidgets.QPushButton(parent=Calculator)
        self.calculator_pushCalculate.setGeometry(QtCore.QRect(260, 560, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_pushCalculate.setFont(font)
        self.calculator_pushCalculate.setStyleSheet("QPushButton{background-color: rgb(220, 220, 220); border: 1px solid gray;}\n"
"QPushButton:hover {background-color: rgb(198, 198, 198)}")
        self.calculator_pushCalculate.setCheckable(True)
        self.calculator_pushCalculate.setChecked(False)
        self.calculator_pushCalculate.setObjectName("calculator_pushCalculate")
        self.calculator_pushSubtract = QtWidgets.QPushButton(parent=Calculator)
        self.calculator_pushSubtract.setGeometry(QtCore.QRect(260, 400, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_pushSubtract.setFont(font)
        self.calculator_pushSubtract.setStyleSheet("QPushButton{background-color: rgb(220, 220, 220); border: 1px solid gray;}\n"
"QPushButton:hover {background-color: rgb(198, 198, 198)}")
        self.calculator_pushSubtract.setCheckable(True)
        self.calculator_pushSubtract.setChecked(False)
        self.calculator_pushSubtract.setObjectName("calculator_pushSubtract")
        self.calculator_operator_buttonGroup.addButton(self.calculator_pushSubtract)
        self.calculator_pushAdd = QtWidgets.QPushButton(parent=Calculator)
        self.calculator_pushAdd.setGeometry(QtCore.QRect(260, 480, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_pushAdd.setFont(font)
        self.calculator_pushAdd.setStyleSheet("QPushButton{background-color: rgb(220, 220, 220); border: 1px solid gray;}\n"
"QPushButton:hover {background-color: rgb(198, 198, 198)}")
        self.calculator_pushAdd.setCheckable(True)
        self.calculator_pushAdd.setChecked(False)
        self.calculator_pushAdd.setObjectName("calculator_pushAdd")
        self.calculator_operator_buttonGroup.addButton(self.calculator_pushAdd)
        self.calculator_pushDivide = QtWidgets.QPushButton(parent=Calculator)
        self.calculator_pushDivide.setGeometry(QtCore.QRect(260, 240, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_pushDivide.setFont(font)
        self.calculator_pushDivide.setStyleSheet("QPushButton{background-color: rgb(220, 220, 220); border: 1px solid gray;}\n"
"QPushButton:hover {background-color: rgb(198, 198, 198)}")
        self.calculator_pushDivide.setCheckable(True)
        self.calculator_pushDivide.setChecked(False)
        self.calculator_pushDivide.setObjectName("calculator_pushDivide")
        self.calculator_operator_buttonGroup.addButton(self.calculator_pushDivide)
        self.calculator_pushSquareRoot = QtWidgets.QPushButton(parent=Calculator)
        self.calculator_pushSquareRoot.setGeometry(QtCore.QRect(180, 240, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_pushSquareRoot.setFont(font)
        self.calculator_pushSquareRoot.setStyleSheet("QPushButton{background-color: rgb(220, 220, 220); border: 1px solid gray;}\n"
"QPushButton:hover {background-color: rgb(198, 198, 198)}")
        self.calculator_pushSquareRoot.setCheckable(True)
        self.calculator_pushSquareRoot.setChecked(False)
        self.calculator_pushSquareRoot.setObjectName("calculator_pushSquareRoot")
        self.calculator_operator_buttonGroup.addButton(self.calculator_pushSquareRoot)
        self.calculator_pushInverse = QtWidgets.QPushButton(parent=Calculator)
        self.calculator_pushInverse.setGeometry(QtCore.QRect(20, 240, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_pushInverse.setFont(font)
        self.calculator_pushInverse.setStyleSheet("QPushButton{background-color: rgb(220, 220, 220); border: 1px solid gray;}\n"
"QPushButton:hover {background-color: rgb(198, 198, 198)}")
        self.calculator_pushInverse.setCheckable(True)
        self.calculator_pushInverse.setChecked(False)
        self.calculator_pushInverse.setObjectName("calculator_pushInverse")
        self.calculator_operator_buttonGroup.addButton(self.calculator_pushInverse)
        self.calculator_pushSquared = QtWidgets.QPushButton(parent=Calculator)
        self.calculator_pushSquared.setGeometry(QtCore.QRect(100, 240, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_pushSquared.setFont(font)
        self.calculator_pushSquared.setStyleSheet("QPushButton{background-color: rgb(220, 220, 220); border: 1px solid gray;}\n"
"QPushButton:hover {background-color: rgb(198, 198, 198)}")
        self.calculator_pushSquared.setCheckable(True)
        self.calculator_pushSquared.setChecked(False)
        self.calculator_pushSquared.setObjectName("calculator_pushSquared")
        self.calculator_operator_buttonGroup.addButton(self.calculator_pushSquared)
        self.calculator_pushBackspace = QtWidgets.QPushButton(parent=Calculator)
        self.calculator_pushBackspace.setGeometry(QtCore.QRect(260, 160, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_pushBackspace.setFont(font)
        self.calculator_pushBackspace.setStyleSheet("QPushButton{background-color: rgb(220, 220, 220); border: 1px solid gray;}\n"
"QPushButton:hover {background-color: rgb(198, 198, 198)}")
        self.calculator_pushBackspace.setCheckable(True)
        self.calculator_pushBackspace.setChecked(False)
        self.calculator_pushBackspace.setObjectName("calculator_pushBackspace")
        self.calculator_pushClear = QtWidgets.QPushButton(parent=Calculator)
        self.calculator_pushClear.setGeometry(QtCore.QRect(180, 160, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_pushClear.setFont(font)
        self.calculator_pushClear.setStyleSheet("QPushButton{background-color: rgb(220, 220, 220); border: 1px solid gray;}\n"
"QPushButton:hover {background-color: rgb(198, 198, 198)}")
        self.calculator_pushClear.setCheckable(True)
        self.calculator_pushClear.setChecked(False)
        self.calculator_pushClear.setObjectName("calculator_pushClear")
        self.calculator_pushMode = QtWidgets.QPushButton(parent=Calculator)
        self.calculator_pushMode.setGeometry(QtCore.QRect(20, 160, 155, 75))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_pushMode.setFont(font)
        self.calculator_pushMode.setStyleSheet("QPushButton{background-color: rgb(220, 220, 220); border: 1px solid gray;}\n"
"QPushButton:hover {background-color: rgb(198, 198, 198)}")
        self.calculator_pushMode.setCheckable(True)
        self.calculator_pushMode.setObjectName("calculator_pushMode")
        self.calculator_screen_tempCalculations = QtWidgets.QLabel(parent=Calculator)
        self.calculator_screen_tempCalculations.setGeometry(QtCore.QRect(20, 20, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.calculator_screen_tempCalculations.setFont(font)
        self.calculator_screen_tempCalculations.setStyleSheet("color:gray")
        self.calculator_screen_tempCalculations.setText("")
        self.calculator_screen_tempCalculations.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.calculator_screen_tempCalculations.setObjectName("calculator_screen_tempCalculations")
        self.area_label_title = QtWidgets.QLabel(parent=Calculator)
        self.area_label_title.setEnabled(False)
        self.area_label_title.setGeometry(QtCore.QRect(360, 20, 311, 131))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.area_label_title.setFont(font)
        self.area_label_title.setStyleSheet("border:1px solid black; border-left: none; border-right: none; border-top: none")
        self.area_label_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.area_label_title.setObjectName("area_label_title")
        self.area_circle_radioButton = QtWidgets.QRadioButton(parent=Calculator)
        self.area_circle_radioButton.setGeometry(QtCore.QRect(360, 160, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.area_circle_radioButton.setFont(font)
        self.area_circle_radioButton.setCheckable(True)
        self.area_circle_radioButton.setChecked(False)
        self.area_circle_radioButton.setAutoExclusive(False)
        self.area_circle_radioButton.setObjectName("area_circle_radioButton")
        self.area_buttonGroup = QtWidgets.QButtonGroup(Calculator)
        self.area_buttonGroup.setObjectName("area_buttonGroup")
        self.area_buttonGroup.addButton(self.area_circle_radioButton)
        self.area_square_radioButton = QtWidgets.QRadioButton(parent=Calculator)
        self.area_square_radioButton.setGeometry(QtCore.QRect(360, 270, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.area_square_radioButton.setFont(font)
        self.area_square_radioButton.setAutoExclusive(False)
        self.area_square_radioButton.setObjectName("area_square_radioButton")
        self.area_buttonGroup.addButton(self.area_square_radioButton)
        self.area_rectangle_radioButton = QtWidgets.QRadioButton(parent=Calculator)
        self.area_rectangle_radioButton.setGeometry(QtCore.QRect(360, 380, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.area_rectangle_radioButton.setFont(font)
        self.area_rectangle_radioButton.setAutoExclusive(False)
        self.area_rectangle_radioButton.setObjectName("area_rectangle_radioButton")
        self.area_buttonGroup.addButton(self.area_rectangle_radioButton)
        self.area_triangle_radioButton = QtWidgets.QRadioButton(parent=Calculator)
        self.area_triangle_radioButton.setGeometry(QtCore.QRect(360, 490, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.area_triangle_radioButton.setFont(font)
        self.area_triangle_radioButton.setAutoExclusive(False)
        self.area_triangle_radioButton.setObjectName("area_triangle_radioButton")
        self.area_buttonGroup.addButton(self.area_triangle_radioButton)
        self.area_circle_input = QtWidgets.QPushButton(parent=Calculator)
        self.area_circle_input.setGeometry(QtCore.QRect(390, 200, 261, 61))
        self.area_circle_input.setStyleSheet("background-color:white; border:1px solid black")
        self.area_circle_input.setCheckable(True)
        self.area_circle_input.setChecked(False)
        self.area_circle_input.setObjectName("area_circle_input")
        self.area_calc_buttonGroup = QtWidgets.QButtonGroup(Calculator)
        self.area_calc_buttonGroup.setObjectName("area_calc_buttonGroup")
        self.area_calc_buttonGroup.addButton(self.area_circle_input)
        self.area_square_input = QtWidgets.QPushButton(parent=Calculator)
        self.area_square_input.setGeometry(QtCore.QRect(390, 310, 261, 61))
        self.area_square_input.setStyleSheet("background-color:white; border:1px solid black")
        self.area_square_input.setCheckable(True)
        self.area_square_input.setObjectName("area_square_input")
        self.area_calc_buttonGroup.addButton(self.area_square_input)
        self.area_rectangle_inputWidth = QtWidgets.QPushButton(parent=Calculator)
        self.area_rectangle_inputWidth.setGeometry(QtCore.QRect(390, 420, 261, 31))
        self.area_rectangle_inputWidth.setStyleSheet("background-color:white; border:1px solid black")
        self.area_rectangle_inputWidth.setCheckable(True)
        self.area_rectangle_inputWidth.setObjectName("area_rectangle_inputWidth")
        self.area_calc_buttonGroup.addButton(self.area_rectangle_inputWidth)
        self.area_rectangle_inputHeight = QtWidgets.QPushButton(parent=Calculator)
        self.area_rectangle_inputHeight.setGeometry(QtCore.QRect(390, 460, 261, 31))
        self.area_rectangle_inputHeight.setStyleSheet("background-color:white; border:1px solid black")
        self.area_rectangle_inputHeight.setCheckable(True)
        self.area_rectangle_inputHeight.setObjectName("area_rectangle_inputHeight")
        self.area_calc_buttonGroup.addButton(self.area_rectangle_inputHeight)
        self.area_triangle_inputHeight = QtWidgets.QPushButton(parent=Calculator)
        self.area_triangle_inputHeight.setGeometry(QtCore.QRect(390, 580, 261, 31))
        self.area_triangle_inputHeight.setStyleSheet("background-color:white; border:1px solid black")
        self.area_triangle_inputHeight.setCheckable(True)
        self.area_triangle_inputHeight.setObjectName("area_triangle_inputHeight")
        self.area_calc_buttonGroup.addButton(self.area_triangle_inputHeight)
        self.area_triangle_inputBase = QtWidgets.QPushButton(parent=Calculator)
        self.area_triangle_inputBase.setGeometry(QtCore.QRect(390, 530, 261, 31))
        self.area_triangle_inputBase.setStyleSheet("background-color:white; border:1px solid black")
        self.area_triangle_inputBase.setCheckable(True)
        self.area_triangle_inputBase.setObjectName("area_triangle_inputBase")
        self.area_calc_buttonGroup.addButton(self.area_triangle_inputBase)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Form"))
        self.calculator_push7.setText(_translate("Calculator", "7"))
        self.calculator_push8.setText(_translate("Calculator", "8"))
        self.calculator_push9.setText(_translate("Calculator", "9"))
        self.calculator_push6.setText(_translate("Calculator", "6"))
        self.calculator_push4.setText(_translate("Calculator", "4"))
        self.calculator_push5.setText(_translate("Calculator", "5"))
        self.calculator_push3.setText(_translate("Calculator", "3"))
        self.calculator_push1.setText(_translate("Calculator", "1"))
        self.calculator_push2.setText(_translate("Calculator", "2"))
        self.calculator_pushTurnNegative.setText(_translate("Calculator", "+ / -"))
        self.calculator_push0.setText(_translate("Calculator", "0"))
        self.calculator_pushDecimal.setText(_translate("Calculator", "."))
        self.calculator_pushMultiply.setText(_translate("Calculator", "x"))
        self.calculator_pushCalculate.setText(_translate("Calculator", "="))
        self.calculator_pushSubtract.setText(_translate("Calculator", "-"))
        self.calculator_pushAdd.setText(_translate("Calculator", "+"))
        self.calculator_pushDivide.setText(_translate("Calculator", "÷"))
        self.calculator_pushSquareRoot.setText(_translate("Calculator", "√x"))
        self.calculator_pushInverse.setText(_translate("Calculator", "1/x"))
        self.calculator_pushSquared.setText(_translate("Calculator", "x²"))
        self.calculator_pushBackspace.setText(_translate("Calculator", "⌫"))
        self.calculator_pushClear.setText(_translate("Calculator", "C"))
        self.calculator_pushMode.setText(_translate("Calculator", "MODE"))
        self.area_label_title.setText(_translate("Calculator", "AREA"))
        self.area_circle_radioButton.setText(_translate("Calculator", "Circle"))
        self.area_square_radioButton.setText(_translate("Calculator", "Square"))
        self.area_rectangle_radioButton.setText(_translate("Calculator", "Rectangle"))
        self.area_triangle_radioButton.setText(_translate("Calculator", "Triangle"))
        self.area_circle_input.setText(_translate("Calculator", "RADIUS"))
        self.area_square_input.setText(_translate("Calculator", "LENGTH"))
        self.area_rectangle_inputWidth.setText(_translate("Calculator", "WIDTH"))
        self.area_rectangle_inputHeight.setText(_translate("Calculator", "HEIGHT"))
        self.area_triangle_inputHeight.setText(_translate("Calculator", "HEIGHT"))
        self.area_triangle_inputBase.setText(_translate("Calculator", "BASE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QWidget()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec())
