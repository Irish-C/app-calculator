# Simple App Calculator
This simple app calculator with **exception handling** will prompt the user to perform one of the four math operations of two numbers repeatedly until they want to exit.
<br/>

Math operations are:
* Addition
* Subtraction
* Multiplication
* Division

## Installation
To run the program, you'll need to have [Python 3](https://www.python.org/downloads/) installed on your computer. <br/>
>**Note: This program might works only for windows os.**
<br/>

I used [VS Code](https://code.visualstudio.com/download) to create and run the program.

## Dependencies
The script requires the following Python packages:
* PySimpleGUI
<br/>
```pip install pySimpleGUI ```
<br/>

## How to make this code works
1. Clone the repository or download the simple_app_calculator.py here.
2. Open a terminal and navigate to the directory containing the script:
``cd /path/to/directory``
3. Run the script using python:
``python simple_app_calculator.py``

## How does the app works
1. Select from the four math operations
> * If user did not select, the math operation error will appear.
2. Enter first number and second number.
> * If user did not enter or entered an invalid value, the invalid error will appear.
> * If the user entered 0 as second number as divisor, the zero division error will appear.
3. Click 'Submit' button and the result will appear.
4. Click 'OK' button and the app will ask if you want to try again.
> * If yes, the program will start again.
> * If no, the program will say 'Thank You!'. Click Exit to terminate the program.
5. The program will run as long as you click 'yes' button.