# import modules
import PySimpleGUI as sg

# Define four math operations function
# Define addition function
def add(a, b):
    return a + b
# Define subtraction function
def subtract(a, b):
    return a - b
# Define multiplication function
def multiply(a, b):
    return a * b
# Define division function
def divide(a, b):
    return a / b

# Define main function
def main():
    sg.theme("DarkTeal10")
    # Define the math_operations window's contents
    layout = [
        [sg.Text('Choose a math operation:')],
        [sg.Radio('Add', 'RADIO1', key='add'), sg.Radio('Subtract', 'RADIO1', key='subtract'),
         sg.Radio('Multiply', 'RADIO1', key='multiply'), sg.Radio('Divide', 'RADIO1', key='divide')],
        [sg.Frame('Inputs', [
            [sg.Text('Enter the first number:'), sg.InputText(key='a')],
            [sg.Text('Enter the second number:'), sg.InputText(key='b')]])],
        [sg.Button('Submit'), sg.Button('Exit')]
    ]

    # Create the math_operations window
    window = sg.Window('APP CALCULATOR', layout)

    # WHILE Start a loop until user choose to exit
    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break

        # TRY calling math operations
        try:
            num1 = float(values['a'])
            num2 = float(values['b'])
            # If "addition", call addition function
            if values['add']:
                result = add(num1, num2)
            # Elif "subtraction", call subtraction function
            elif values['subtract']:
                result = subtract(num1, num2)
            # Elif "multiplication", call multiplication function
            elif values['multiply']:
                result = multiply(num1, num2)
            # Elif "division", call division function
            elif values['divide']:
                # If ZeroDivisionError, raise it
                if num2 == 0:
                    raise ZeroDivisionError
                result = divide(num1, num2)
            # Else, user did not choose any math operations
            else:
                sg.popup("Please select a math operation.", title="Math Operation Error")

            # Create Pop-Up to display result
            sg.popup(f'The result is: {result}', title='Result', button_type=sg.BUTTON_OK)
 
        # exception for ZeroDivisionError using Pop-up
        except ValueError:
            sg.popup('Invalid input. Please enter valid numbers.', title='Error')
        # exception for ValueError using Pop-up
        except ZeroDivisionError:
            sg.popup("Cannot divide by zero. Please enter a different second number.", title="Error")

            # Define the try_again window's contents
            # Display try_again window
                # TRY Ask the user wants to try again or not
                # If "yes", repeat start loop
                # If "no", program will exit or if window is closed

# Close the window