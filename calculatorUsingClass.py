class Calculator:
    def __init__(self) -> None:
        self.equation = ''

    def isOperator(self, character):
        if ((character=="+") or ( character == "-") or( character=="/") or ( character == "*") or (character=="%")):
            return True
        else:
            return False

    def takeUserInput(self, userInput):
        self.userInput = userInput

    def Validate(self):
        if self.userInput == "q" or self.userInput=="Q":
            print("Exiting cmdline calculator. Thank you.")
            quit()
        elif self.userInput == 's' or self.userInput =='S':
            print(f"Current equation is: {self.equation}")
        elif self.userInput == "c" or self.userInput == "C":
            self.equation = ''
        elif self.userInput == '=':
            try:
                solution = eval(self.equation)
                print(f"Current val= {solution}")
            except Exception as e:
                print("Invalid equation, enter again")
        else:
            if ((self.equation != '') and (self.isOperator(self.equation[-1])) and (self.isOperator(self.userInput))):
                print("Invalid operator, enter again")
            elif ((self.equation != '') and (self.equation[-1].isnumeric()) and (self.userInput.isnumeric())):
                self.equation = self.userInput
            elif ((self.userInput.isnumeric()) or (self.isOperator(self.userInput)) or (self.userInput==".")):
                if((self.equation == '' )and (self.isOperator(self.userInput))):
                    pass
                elif self.equation == '':
                    self.equation = self.userInput
                else:
                    self.equation += self.userInput
            else:
                print("invalid character")

calculator = Calculator()

while True:
    userInput = input("Enter number or operator: ")
    calculator.takeUserInput(userInput)
    calculator.Validate()