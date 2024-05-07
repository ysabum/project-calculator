from PyQt6.QtWidgets import *
from gui import *
from graphics.resources import *
import functions

class Logic(QMainWindow, Ui_Calculator):
    '''
    Class for adding logic for Calculator GUI.
    '''
    
    def __init__(self) -> None:
        '''
        Initializes Logic object.
        '''
        
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        QWidget.resize(self, 350, 650)
        QWidget.setMinimumSize(self, QtCore.QSize(350, 650))
        QWidget.setMaximumSize(self, QtCore.QSize(350, 650))
        
        self.Calculator_Calculations_listed = []
        self.Calculator_Calculations = ''
        self.Calculator_Screen = ''
        self.calculator_screen.setText('0')
        
        # Button events
        self.calculator_pushNumeric_buttonGroup.buttonClicked.connect(lambda:self.push_number())
        
        self.calculator_pushAdd.clicked.connect(lambda:self.push_add())
        self.calculator_pushSubtract.clicked.connect(lambda:self.push_subtract())
        self.calculator_pushDivide.clicked.connect(lambda:self.push_divide())
        self.calculator_pushMultiply.clicked.connect(lambda:self.push_multiply())
        
        self.calculator_pushInverse.clicked.connect(lambda:self.push_inverse())
        self.calculator_pushSquared.clicked.connect(lambda:self.push_squared())
        self.calculator_pushSquareRoot.clicked.connect(lambda:self.push_squareroot())
        
        self.calculator_pushClear.clicked.connect(lambda:self.push_clear())
        self.calculator_pushCalculate.clicked.connect(lambda:self.push_calculate())
        self.calculator_pushBackspace.clicked.connect(lambda:self.push_delete())
        
        # Mode events
        self.calculator_pushMode.clicked.connect(lambda:self.push_mode())
        self.area_buttonGroup.buttonClicked.connect(lambda:self.push_area())
        self.area_calc_buttonGroup.buttonClicked.connect(lambda:self.push_calc_area())
        
        self.area_circle_input.setVisible(False)
        self.area_square_input.setVisible(False)
        self.area_rectangle_inputWidth.setVisible(False)
        self.area_rectangle_inputHeight.setVisible(False)
        self.area_triangle_inputBase.setVisible(False)
        self.area_triangle_inputHeight.setVisible(False)
        
        
    def push_clear(self) -> None:
        '''
        Method when user pushes the clear button.
        Clears data on calculator screen and resets to default.
        '''
        
        self.Calculator_Screen = ''
        self.calculator_screen_tempCalculations.setText('')  
        self.calculator_screen.setText('0')
        
    
    def push_delete(self) -> None:
        '''
        Method called when user pushes the backspace button.
        '''
        
        delete_calculator_screen = self.calculator_screen.text()
        
        if len(delete_calculator_screen) > 0 and 'ERROR' not in delete_calculator_screen:
            delete_calculator_screen = delete_calculator_screen.removesuffix(delete_calculator_screen[-1])
            self.calculator_screen.setText(delete_calculator_screen)
            
    
    def push_mode(self) -> None:
        '''
        Method called when user pushes the 'Mode' button.
        '''
        
        if self.calculator_pushMode.isChecked() and self.area_label_title.isEnabled() == False:
            QWidget.setMinimumSize(self, QtCore.QSize(700, 650))
            QWidget.setMaximumSize(self, QtCore.QSize(700, 650))
            QWidget.resize(self, 700, 650)
            
            self.area_label_title.setEnabled(True)
            
            # Disable operators
            self.calculator_pushInverse.setEnabled(False)
            self.calculator_pushSquared.setEnabled(False)
            self.calculator_pushSquareRoot.setEnabled(False)
            self.calculator_pushDivide.setEnabled(False)
            self.calculator_pushMultiply.setEnabled(False)
            self.calculator_pushSubtract.setEnabled(False)
            self.calculator_pushAdd.setEnabled(False)
            
        else:
            QWidget.resize(self, 350, 650)
            QWidget.setMinimumSize(self, QtCore.QSize(350, 650))
            QWidget.setMaximumSize(self, QtCore.QSize(350, 650))
            
            self.area_label_title.setEnabled(False)
            
            self.area_circle_input.setVisible(False)
            self.area_square_input.setVisible(False)
            self.area_rectangle_inputWidth.setVisible(False)
            self.area_rectangle_inputHeight.setVisible(False)
            self.area_triangle_inputBase.setVisible(False)
            self.area_triangle_inputHeight.setVisible(False)
            
            # Enable operators
            self.calculator_pushInverse.setEnabled(True)
            self.calculator_pushSquared.setEnabled(True)
            self.calculator_pushSquareRoot.setEnabled(True)
            self.calculator_pushDivide.setEnabled(True)
            self.calculator_pushMultiply.setEnabled(True)
            self.calculator_pushSubtract.setEnabled(True)
            self.calculator_pushAdd.setEnabled(True)
                
    
    def push_area(self) -> None:
        '''
        Method called when user clicks one of the 'Area' radio buttons.
        '''
        
        if self.area_circle_radioButton.isChecked():
            self.area_circle_input.setVisible(True)
            self.area_square_input.setVisible(False)
            self.area_rectangle_inputWidth.setVisible(False)
            self.area_rectangle_inputHeight.setVisible(False)
            self.area_triangle_inputBase.setVisible(False)
            self.area_triangle_inputHeight.setVisible(False)
            
            self.area_circle_input.setText('RADIUS')
            self.area_square_input.setText('LENGTH')
            self.area_rectangle_inputWidth.setText('WIDTH')
            self.area_rectangle_inputHeight.setText('HEIGHT')
            self.area_triangle_inputBase.setText('BASE')
            self.area_triangle_inputHeight.setText('HEIGHT')
            
        elif self.area_square_radioButton.isChecked():
            self.area_circle_input.setVisible(False)
            self.area_square_input.setVisible(True)
            self.area_rectangle_inputWidth.setVisible(False)
            self.area_rectangle_inputHeight.setVisible(False)
            self.area_triangle_inputBase.setVisible(False)
            self.area_triangle_inputHeight.setVisible(False)
            
            self.area_circle_input.setText('RADIUS')
            self.area_square_input.setText('LENGTH')
            self.area_rectangle_inputWidth.setText('WIDTH')
            self.area_rectangle_inputHeight.setText('HEIGHT')
            self.area_triangle_inputBase.setText('BASE')
            self.area_triangle_inputHeight.setText('HEIGHT')
            
        elif self.area_rectangle_radioButton.isChecked():
            self.area_circle_input.setVisible(False)
            self.area_square_input.setVisible(False)
            self.area_rectangle_inputWidth.setVisible(True)
            self.area_rectangle_inputHeight.setVisible(True)
            self.area_triangle_inputBase.setVisible(False)
            self.area_triangle_inputHeight.setVisible(False)
            
            self.area_circle_input.setText('RADIUS')
            self.area_square_input.setText('LENGTH')
            self.area_rectangle_inputWidth.setText('WIDTH')
            self.area_rectangle_inputHeight.setText('HEIGHT')
            self.area_triangle_inputBase.setText('BASE')
            self.area_triangle_inputHeight.setText('HEIGHT')
            
        elif self.area_triangle_radioButton.isChecked():
            self.area_circle_input.setVisible(False)
            self.area_square_input.setVisible(False)
            self.area_rectangle_inputWidth.setVisible(False)
            self.area_rectangle_inputHeight.setVisible(False)
            self.area_triangle_inputBase.setVisible(True)
            self.area_triangle_inputHeight.setVisible(True)
            
            self.area_circle_input.setText('RADIUS')
            self.area_square_input.setText('LENGTH')
            self.area_rectangle_inputWidth.setText('WIDTH')
            self.area_rectangle_inputHeight.setText('HEIGHT')
            self.area_triangle_inputBase.setText('BASE')
            self.area_triangle_inputHeight.setText('HEIGHT')
            
    
    def push_calc_area(self) -> None:
        '''
        Method called when user clicks one of the 'Area' buttons (radius, height, etc.).
        '''
            
        if self.area_circle_input.isChecked():
            self.area_circle_input.setChecked(False)
            self.area_circle_input.setText(self.calculator_screen.text())
            
            self.Calculator_Screen = ''
            
        elif self.area_square_input.isChecked():
            self.area_square_input.setChecked(False)
            self.area_square_input.setText(self.calculator_screen.text())
            
            self.Calculator_Screen = ''
        
        elif self.area_rectangle_inputWidth.isChecked():
            self.area_rectangle_inputWidth.setChecked(False)
            self.area_rectangle_inputWidth.setText(self.calculator_screen.text())
            
            self.Calculator_Screen = ''
            
        elif self.area_rectangle_inputHeight.isChecked():
            self.area_rectangle_inputHeight.setChecked(False)
            self.area_rectangle_inputHeight.setText(self.calculator_screen.text())
            
            self.Calculator_Screen = ''
            
        elif self.area_triangle_inputBase.isChecked():
            self.area_triangle_inputBase.setChecked(False)
            self.area_triangle_inputBase.setText(self.calculator_screen.text())
            
            self.Calculator_Screen = ''
            
        elif self.area_triangle_inputHeight.isChecked():
            self.area_triangle_inputHeight.setChecked(False)
            self.area_triangle_inputHeight.setText(self.calculator_screen.text())
            
            self.Calculator_Screen = ''
            
            
    def push_number(self) -> None:
        '''
        Method called when user pushes either a number, the decimal point, or the negative/positive symbol on the calculator.
        '''
        
        # Numeric operands
        if self.calculator_push0.isChecked():
            self.calculator_push0.setChecked(False)
            
            if self.calculator_screen.text() == '0' or self.Calculator_Screen == '': ### Maybe a temp fix?
                self.calculator_screen.setText('0')
            else:
                self.Calculator_Screen += '0'
                self.calculator_screen.setText(self.Calculator_Screen)
            
        elif self.calculator_push1.isChecked():
            self.calculator_push1.setChecked(False)
            self.Calculator_Screen += '1'
            self.calculator_screen.setText(self.Calculator_Screen)
            
        elif self.calculator_push2.isChecked():
            self.calculator_push2.setChecked(False)
            self.Calculator_Screen += '2'
            self.calculator_screen.setText(self.Calculator_Screen)
            
        elif self.calculator_push3.isChecked():
            self.calculator_push3.setChecked(False)
            self.Calculator_Screen += '3'
            self.calculator_screen.setText(self.Calculator_Screen)
            
        elif self.calculator_push4.isChecked():
            self.calculator_push4.setChecked(False)
            self.Calculator_Screen += '4'
            self.calculator_screen.setText(self.Calculator_Screen)
            
        elif self.calculator_push5.isChecked():
            self.calculator_push5.setChecked(False)
            self.Calculator_Screen += '5'
            self.calculator_screen.setText(self.Calculator_Screen)
            
        elif self.calculator_push6.isChecked():
            self.calculator_push6.setChecked(False)
            self.Calculator_Screen += '6'
            self.calculator_screen.setText(self.Calculator_Screen)
            
        elif self.calculator_push7.isChecked():
            self.calculator_push7.setChecked(False)
            self.Calculator_Screen += '7'
            self.calculator_screen.setText(self.Calculator_Screen)
            
        elif self.calculator_push8.isChecked():
            self.calculator_push8.setChecked(False)
            self.Calculator_Screen += '8'
            self.calculator_screen.setText(self.Calculator_Screen)
            
        elif self.calculator_push9.isChecked():
            self.calculator_push9.setChecked(False)
            self.Calculator_Screen += '9'
            self.calculator_screen.setText(self.Calculator_Screen)
         
        # Other 
        elif self.calculator_pushDecimal.isChecked():
            if '.' in self.calculator_screen.text():
                pass
            
            else:
                if self.calculator_screen.text() == '0':
                    self.Calculator_Screen = '0.'
                    self.calculator_screen.setText(self.Calculator_Screen)
                    
                else:
                    self.Calculator_Screen += '.'
                    self.calculator_screen.setText(self.Calculator_Screen)
        
        elif self.calculator_pushTurnNegative.isChecked():
            self.calculator_pushTurnNegative.setChecked(False)
            numerics_nonzero = ['1','2','3','4','5','6','7','8','9']
            
            if self.calculator_screen.text() == '0' or (self.calculator_screen.text().startswith('0.') and not any(number in self.calculator_screen.text() for  number in numerics_nonzero)):
                pass
            
            else:
                if 'ERROR' in self.calculator_screen.text():
                    pass
                
                elif '-' in self.calculator_screen.text():
                    self.calculator_screen.setText(self.calculator_screen.text().removeprefix('-'))
                    
                else:
                    self.calculator_screen.setText('-' + self.calculator_screen.text())
                
    
    def push_add(self) -> None:
        '''
        Method called when user pushes the +(add) button.
        '''
        
        self.Calculator_Screen = '' # Resets calculator to default (0) like as seen in method push_clear.
        self.calculator_screen_tempCalculations.setText('')
        self.Calculator_Calculations = ''
        self.Calculator_Calculations_listed = []
            
        self.Calculator_Calculations_listed.append(self.calculator_screen.text())
        self.Calculator_Calculations_listed.append('+')
        
        max_history_length = 2
        history_length = 0
        
        while history_length < 2:
            for item in self.Calculator_Calculations_listed:
                self.Calculator_Calculations += item + ' '
                history_length += 1
            break
            
        self.calculate()
        
    
    def push_subtract(self) -> None:
        '''
        Method called when user pushes the -(subtract) button.
        '''
        
        self.Calculator_Screen = ''
        self.calculator_screen_tempCalculations.setText('')
        self.Calculator_Calculations = ''
        self.Calculator_Calculations_listed = []
            
        self.Calculator_Calculations_listed.append(self.calculator_screen.text())
        self.Calculator_Calculations_listed.append('-')
        
        max_history_length = 2
        history_length = 0
        
        while history_length < 2:
            for item in self.Calculator_Calculations_listed:
                self.Calculator_Calculations += item + ' '
                history_length += 1
            break
            
        self.calculate()
        
    
    def push_divide(self) -> None:
        '''
        Method called when user pushes the ÷(divide) button.
        '''
        
        self.Calculator_Screen = ''
        self.calculator_screen_tempCalculations.setText('')
        self.Calculator_Calculations = ''
        self.Calculator_Calculations_listed = []
            
        self.Calculator_Calculations_listed.append(self.calculator_screen.text())
        self.Calculator_Calculations_listed.append('÷')
        
        max_history_length = 2
        history_length = 0
        
        while history_length < 2:
            for item in self.Calculator_Calculations_listed:
                self.Calculator_Calculations += item + ' '
                history_length += 1
            break
            
        self.calculate()
    
    
    def push_multiply(self) -> None:
        '''
        Method called when user pushes the x(multiply) button.
        '''
        
        self.Calculator_Screen = ''
        self.calculator_screen_tempCalculations.setText('')
        self.Calculator_Calculations = ''
        self.Calculator_Calculations_listed = []
            
        self.Calculator_Calculations_listed.append(self.calculator_screen.text())
        self.Calculator_Calculations_listed.append('x')
        
        max_history_length = 2
        history_length = 0
        
        while history_length < 2:
            for item in self.Calculator_Calculations_listed:
                self.Calculator_Calculations += item + ' '
                history_length += 1
            break
            
        self.calculate()
        
        
    def push_inverse(self) -> None:
        '''
        Method called when user pushes the 1/x(inverse) button.
        '''
        
        self.Calculator_Screen = ''
        self.calculator_screen_tempCalculations.setText('')
        self.Calculator_Calculations = ''
        self.Calculator_Calculations_listed = []
        
        self.Calculator_Calculations_listed.append('1')
        self.Calculator_Calculations_listed.append('/')
        self.Calculator_Calculations_listed.append(self.calculator_screen.text())
        self.Calculator_Calculations_listed.append('=')
        
        max_history_length = 4
        history_length = 0
        
        while history_length < 4:
            for item in self.Calculator_Calculations_listed:
                self.Calculator_Calculations += item + ' '
                history_length += 1
            break
            
        self.calculate()
        
        
    def push_squared(self) -> None:
        '''
        Method called when user pushes the x²(squared) button.
        '''
        
        self.Calculator_Screen = ''
        self.calculator_screen_tempCalculations.setText('')
        self.Calculator_Calculations = ''
        self.Calculator_Calculations_listed = []
        
        self.Calculator_Calculations_listed.append(self.calculator_screen.text())
        self.Calculator_Calculations_listed.append('^')
        self.Calculator_Calculations_listed.append('2')
        self.Calculator_Calculations_listed.append('=')
        
        max_history_length = 4
        history_length = 0
        
        while history_length < 4:
            for item in self.Calculator_Calculations_listed:
                self.Calculator_Calculations += item + ' '
                history_length += 1
            break
            
        self.calculate()
        
    
    def push_squareroot(self) -> None:
        '''
        Method called when user pushes the √x(square root) button.
        '''
        
        self.Calculator_Screen = ''
        self.calculator_screen_tempCalculations.setText('')
        self.Calculator_Calculations = ''
        self.Calculator_Calculations_listed = []
        
        self.Calculator_Calculations_listed.append(self.calculator_screen.text())
        self.Calculator_Calculations_listed.append('^')
        self.Calculator_Calculations_listed.append('0.5')
        self.Calculator_Calculations_listed.append('=')
        
        max_history_length = 4
        history_length = 0
        
        while history_length < 4:
            for item in self.Calculator_Calculations_listed:
                self.Calculator_Calculations += item + ' '
                history_length += 1
            break
            
        self.calculate()
        
        
    def push_calculate(self) -> None:
        '''
        Method called when user pushes the calculate/equal button.
        '''
        
        if self.area_label_title.isEnabled():
            self.push_area_calculate()
            
        else:
            self.Calculator_Screen = '' 
            self.calculator_screen_tempCalculations.setText('')
            self.Calculator_Calculations = ''
                
            self.Calculator_Calculations_listed.append(self.calculator_screen.text())
            self.Calculator_Calculations_listed.append('=')   
            max_history_length = 4
            history_length = 0
                
            while history_length < 4:
                for item in self.Calculator_Calculations_listed:
                    self.Calculator_Calculations += item + ' '
                    history_length += 1
                        
                break
                    
            self.calculate()
    
    
    def calculate(self) -> None:
        '''
        Method for calculating input from the calculator GUI.
        '''
        
        valid_basic_operators = ['-', '÷', '+', 'x', '/', '^']
        operand_1 = self.Calculator_Calculations_listed[0]
        operator_1 = self.Calculator_Calculations_listed[1]
        
        try:
            if len(self.Calculator_Calculations_listed) == 2:
                if operator_1 == '=':
                    self.calculator_screen_tempCalculations.setText(self.Calculator_Calculations)
                    self.calculator_screen.setText(operand_1)
                    self.Calculator_Calculations_listed = []
                    
                elif operator_1 in valid_basic_operators:
                    self.calculator_screen_tempCalculations.setText(self.Calculator_Calculations)
                    self.calculator_screen.setText(operand_1)
            
            else:
                operand_2 = self.Calculator_Calculations_listed[2]
                operator_2 = self.Calculator_Calculations_listed[3]
                
                # Addition 
                if operator_1 == '+': 
                    answer = functions.add(operand_1, operand_2)
                    
                    self.calculator_screen_tempCalculations.setText(self.Calculator_Calculations)
                    self.calculator_screen.setText(str(answer))
                    
                # Subtraction
                elif operator_1 == '-': 
                    answer = functions.subtract(operand_1, operand_2)
                    
                    self.calculator_screen_tempCalculations.setText(self.Calculator_Calculations)
                    self.calculator_screen.setText(str(answer))
                    
                # Division
                elif operator_1 == '÷' or operator_1 == '/':
                    answer = functions.divide(operand_1, operand_2)
                    
                    self.calculator_screen_tempCalculations.setText(self.Calculator_Calculations)
                    self.calculator_screen.setText(str(answer))
                
                # Multiplication
                elif operator_1 == 'x': 
                    answer = functions.multiply(operand_1, operand_2)
                    
                    self.calculator_screen_tempCalculations.setText(self.Calculator_Calculations)
                    self.calculator_screen.setText(str(answer))
                
                # Squared
                elif operator_1 == '^':
                    answer = functions.squared(operand_1, operand_2)
                    
                    self.calculator_screen_tempCalculations.setText(self.Calculator_Calculations)
                    self.calculator_screen.setText(str(answer))
                    
                self.Calculator_Calculations_listed = []
                
        except:
            self.calculator_screen.setText('ERROR')
            self.Calculator_Calculations_listed = []
            
            
    def push_area_calculate(self) -> None:
        '''
        Method for calculating input from the calculator GUI while 'Mode' is selected.
        '''
        
        try:
            if self.area_circle_radioButton.isChecked():
                radius = self.area_circle_input.text()
                self.calculator_screen.setText(str(functions.circle(radius)))
                
            elif self.area_square_radioButton.isChecked():
                length = self.area_square_input.text()
                self.calculator_screen.setText(str(functions.square(length)))
                
            elif self.area_rectangle_radioButton.isChecked():
                width = self.area_rectangle_inputWidth.text()
                height = self.area_rectangle_inputHeight.text()
                self.calculator_screen.setText(str(functions.rectangle(width, height)))
                
            elif self.area_triangle_radioButton.isChecked():
                base = self.area_triangle_inputBase.text()
                height = self.area_triangle_inputHeight.text()
                self.calculator_screen.setText(str(functions.triangle(base, height)))
                
        except TypeError:
            self.calculator_screen.setText('ERROR: Numbers must be positive')
                
        except:
            self.calculator_screen.setText('ERROR')