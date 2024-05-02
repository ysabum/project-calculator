from PyQt6.QtWidgets import *
from gui import *

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
        
        self.Calculator_Calculations_listed = []
        self.Calculator_Calculations = ''
        self.Calculator_Screen = ''
        self.calculator_screen.setText('0')
        
        # Button events
        self.calculator_pushNumeric_buttonGroup.buttonClicked.connect(lambda:self.push_number())
        self.calculator_pushBasicOperator_buttonGroup.buttonClicked.connect(lambda:self.push_operator())
        
        self.calculator_pushClear.clicked.connect(lambda:self.push_clear())
        self.calculator_pushCalculate.clicked.connect(lambda:self.push_calculate())
    
    
    def push_number(self) -> None:
        '''
        Method when user pushes either a number, the decimal point, or the negative/positive symbol on the calculator.
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
                
    
    def push_operator(self) -> None:
        '''
        Method when user pushes a basic operator button (+/-/x/÷).
        '''
        
        pass
    
        self.Calculator_Screen = '' # Resets calculator to default (0) like as seen in method push_clear.
        
        self.calculator_screen_tempCalculations.setText('')
        self.Calculator_Calculations_listed = []
        self.Calculator_Calculations = ''
        
        self.Calculator_Calculations_listed.append(self.calculator_screen.text())
        self.Calculator_Calculations_listed.append('=')   
        max_history_length = 4
        history_length = 0
        
        
    def push_clear(self) -> None:
        '''
        Method when user pushes the clear button on the calculator.
        Clears data on calculator screen and resets to default.
        '''
        
        self.Calculator_Screen = ''
        self.calculator_screen_tempCalculations.setText('')  
        self.calculator_screen.setText('0')
        
        
    def push_calculate(self) -> None:
        '''
        Method when user pushes the calculate/equal button on the calculator.
        '''
        
        self.Calculator_Screen = '' # Resets calculator to default (0) like as seen in method push_clear.
        self.calculator_screen_tempCalculations.setText('')
        
        if '=' in self.Calculator_Calculations_listed:
            self.Calculator_Calculations_listed = []
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
            
        self.calculator_screen_tempCalculations.setText(self.Calculator_Calculations)
        self.calculate()
    
    
    def calculate(self) -> None:
        '''
        Method for calculating input from the calculator.
        '''
    
        if len(self.Calculator_Calculations_listed) == 2:
            operand_1 = self.Calculator_Calculations_listed[0]
            operator_1 = self.Calculator_Calculations_listed[1]
            if operator_1 == '=':
                answer = operand_1
                self.calculator_screen.setText(answer)