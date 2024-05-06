from PyQt6.QtWidgets import *
from gui import *
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
        
        self.calculator_pushMode.clicked.connect(lambda:self.push_mode())
    
    
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
        
        if len(delete_calculator_screen) > 0 and delete_calculator_screen != 'ERROR':
            delete_calculator_screen = delete_calculator_screen.removesuffix(delete_calculator_screen[-1])
            self.calculator_screen.setText(delete_calculator_screen)
            
    
    def push_mode(self) -> None:
        '''
        Method called when user pushed the Mode button.
        '''
        
        if QWidget.frameGeometry(self).width() == 350:
            QWidget.resize(self, 700, 650)
        else:
            QWidget.resize(self, 350, 650)
            
    
    def push_number(self) -> None:
        '''
        Method called when user pushes either a number, the decimal point, or the negative/positive symbol on the calculator.
        '''
        
        # Numeric operands
        if self.calculator_push0.isChecked() == True:
            self.calculator_push0.isChecked() == False
            
            if self.calculator_screen.text() == '0' or self.Calculator_Screen == '': ### Maybe a temp fix?
                self.calculator_screen.setText('0')
            else:
                self.Calculator_Screen += '0'
                self.calculator_screen.setText(self.Calculator_Screen)
            
        elif self.calculator_push1.isChecked() == True:
            self.calculator_push1.isChecked() == False
            self.Calculator_Screen += '1'
            self.calculator_screen.setText(self.Calculator_Screen)
            
        elif self.calculator_push2.isChecked() == True:
            self.calculator_push2.isChecked() == False
            self.Calculator_Screen += '2'
            self.calculator_screen.setText(self.Calculator_Screen)
            
        elif self.calculator_push3.isChecked() == True:
            self.calculator_push3.isChecked() == False
            self.Calculator_Screen += '3'
            self.calculator_screen.setText(self.Calculator_Screen)
            
        elif self.calculator_push4.isChecked() == True:
            self.calculator_push4.isChecked() == False
            self.Calculator_Screen += '4'
            self.calculator_screen.setText(self.Calculator_Screen)
            
        elif self.calculator_push5.isChecked() == True:
            self.calculator_push5.isChecked() == False
            self.Calculator_Screen += '5'
            self.calculator_screen.setText(self.Calculator_Screen)
            
        elif self.calculator_push6.isChecked() == True:
            self.calculator_push6.isChecked() == False
            self.Calculator_Screen += '6'
            self.calculator_screen.setText(self.Calculator_Screen)
            
        elif self.calculator_push7.isChecked() == True:
            self.calculator_push7.isChecked() == False
            self.Calculator_Screen += '7'
            self.calculator_screen.setText(self.Calculator_Screen)
            
        elif self.calculator_push8.isChecked() == True:
            self.calculator_push8.isChecked() == False
            self.Calculator_Screen += '8'
            self.calculator_screen.setText(self.Calculator_Screen)
            
        elif self.calculator_push9.isChecked() == True:
            self.calculator_push9.isChecked() == False
            self.Calculator_Screen += '9'
            self.calculator_screen.setText(self.Calculator_Screen)
         
        # Other 
        elif self.calculator_pushDecimal.isChecked() == True:
            if '.' in self.calculator_screen.text():
                pass
            else:
                if self.calculator_screen.text() == '0':
                    self.Calculator_Screen = '0.'
                    self.calculator_screen.setText(self.Calculator_Screen)
                else:
                    self.Calculator_Screen += '.'
                    self.calculator_screen.setText(self.Calculator_Screen)
        
        elif self.calculator_pushTurnNegative.isChecked() == True:
            self.calculator_pushTurnNegative.isChecked() == False
            numerics_nonzero = ['1','2','3','4','5','6','7','8','9']
            
            if self.calculator_screen.text() == '0' or (self.calculator_screen.text().startswith('0.') and not any(number in self.calculator_screen.text() for  number in numerics_nonzero)):
                pass
            else:
                if '-' in self.Calculator_Screen:
                    self.Calculator_Screen = self.Calculator_Screen.removeprefix('-')
                else:
                    self.Calculator_Screen = '-' + self.Calculator_Screen
                    
                self.calculator_screen.setText(self.Calculator_Screen)
                
    
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
        Method called when user pushes the 1/x(inverse) button.
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
        Method called when user pushes the 1/x(inverse) button.
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
                    pass
            
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