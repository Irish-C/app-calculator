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
            [sg.Text('Enter the first number:'), sg.InputText(key='first')],
            [sg.Text('Enter the second number:'), sg.InputText(key='second')]])],
        [sg.Button('Submit'), sg.Button('Exit')]
    ]

    # Create the math_operations window
    window = sg.Window('APP CALCULATOR', layout)

    # WHILE Start a loop until user choose to exit
        # Ask the user to choose one of the four math operations
            # TRY calling math operations
                # If "addition", call addition function
                # Elif "subtraction", call subtraction function
                # Elif "multiplication", call multiplication function
                # Elif "division", call division function
                    # If ZeroDivisionError, raise it

                # Else, user did not choose any math operations
                # exception for ZeroDivisionError using Pop-up
                # exception for ValueError using Pop-up
            
            # Create Pop-Up to display result
                # If the user choose exit window, exit the window
            # Close the Pop-up

            # Define the try_again window's contents
            # Display try_again window
                # TRY Ask the user wants to try again or not
                # If "yes", repeat start loop
                # If "no", program will exit or if window is closed

# Close the window