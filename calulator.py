# Functions
def isOperator(string):
    if ((string=="+") or ( string == "-") or( string=="/") or ( string == "*") or (string=="%")):
        return True
    else:
        return False

# Global Variables
equation = ''

# Running a while loop until unless user don't press the q or Q 
while True:
    userInput = input("Enter number or operator: ") # Taking input from user
    # If user Press q or Q then print something and break the loop
    if userInput == "q" or userInput=="Q":
        print("Exiting cmdline calculator. Thank you.")
        break
    # if user press the s or S then show the current equation
    elif userInput == 's' or userInput =='S':
        print(f"Current equation is: {equation}")
    # if user press c or C then reset the equation
    elif userInput == "c" or userInput == "C":
        equation = ''
    # if user press = then show the solution of the equation
    elif userInput == '=':
        try:
            # solution = sympy.sympify(equation)
            solution = eval(equation)
            print(f"Current val= {solution}")
        except Exception as e:
            print("Invalid Equation, enter again")
    # otherwise
    else:
        # user press any operator if an operator was already presses by user then show warning
        if ((equation != '') and (isOperator(equation[-1])) and (isOperator(userInput))):
            print("Invalid operator, enter again")
        # user inputs number if last input is also number then replace the equation with new number
        elif ((equation != '') and (equation[-1].isnumeric()) and (userInput.isnumeric())):
            equation = userInput
        # if user input is number or . then add it to the equation
        elif ((userInput.isnumeric()) or (isOperator(userInput)) or (userInput==".")):
            if((equation == '' )and (isOperator(userInput))):
                continue
            elif equation == '':
                equation = userInput
            else:
                equation += userInput
        # if user inputs anything instead of 0 - 9  or . then show warning
        else:
            print("invalid character")