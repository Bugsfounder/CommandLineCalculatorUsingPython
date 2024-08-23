# Command Line Calculator Program

## Abstract
This project is a **Command Line Calculator** capable of performing basic mathematical operations like addition, subtraction, division, and multiplication. The calculator appends operations to the current result unless the user requests a reset. It has been developed with a focus on good usage of **OOP design**, **C++ STL**, and follows clear naming and coding guidelines.

## Functional Requirements

1. **Validate Input**: Ensure that all user inputs are valid numbers or operators.
2. **Output on "="**: Display the result of the current equation when the user inputs `=`.
3. **Reset on "C"**: Clear the current equation when the user inputs `c` or `C`.
4. **Exit on "Q"**: Exit the program when the user inputs `q` or `Q`.
5. **Show Current Equation**: Display the current equation in memory when the user inputs `s` or `S`.

## Example Use Case

```bash
Current Equation in Memory (not displayed on console)
Enter number or operator: 12 ()
Enter number or operator: + (12)
Enter number or operator: 34 (12 + 34)
Enter number or operator: 45 (45)
Enter number or operator: = (45)
Current val = 45
Enter number or operator: / (45)
Enter number or operator: / (45/)
Invalid operator, enter again
Enter number or operator: s (45/)
Current equation is: 45/
Enter number or operator: 23 (45/23)
Enter number or operator: = (45/23)
Current val = 1.956521739
Enter number or operator: + (45/23)
Enter number or operator: 49 (45/23 + 49)
Current val = 50.956521739 (45/23 + 49)
Enter number or operator: * (45/23 + 49)
Enter number or operator: 3 (45/23 + 49 * 3)
Enter number or operator: = (45/23 + 49 * 3)
Current val = 148.956521739 (45/23 + 49 * 3)
Enter number or operator: C (Clears the equation)
Enter number or operator: 1 ()
Enter number or operator: q (Exits the program)
Exiting command line calculator. Thank you.
```


## Key Features

- **Basic Operations**: Addition, subtraction, division, multiplication.
- **Continuous Calculation**: Appends the next operation to the current result unless reset.
- **Input Validation**: Ensures valid operators and numbers.
- **User Commands**:
  - `=`: Evaluate the current equation.
  - `c/C`: Clear the current equation.
  - `q/Q`: Exit the program.
  - `s/S`: Display the current equation in memory.

## OOP Design & C++ STL
This project emphasizes a well-structured Object-Oriented Design to enhance maintainability and extensibility, leveraging C++ Standard Template Library (STL) for efficient management of data and operations.

## How to Run
- Compile the code using a C++ compiler.
- Execute the program and follow the prompts to enter numbers and operators.


