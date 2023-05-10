# import modules
import PySimpleGUI as sg

# Define addition function
def add(a, b):
    return round(a + b, 2)
# Define subtraction function
def subtract(a, b):
    return round(a - b, 2)
# Define multiplication function
def multiply(a, b):
    return round(a * b, 2)
# Define division function
def divide(a, b):
    return round(a / b, 2)

# Define main function
def main():
    sg.theme("GreenTan")
    # Define the math_operations window's contents
    layout = [
        [sg.Text('Select a math operation:')],
        [sg.Radio('Add', 'RADIO1', key='add'), sg.Radio('Subtract', 'RADIO1', key='subtract'),
         sg.Radio('Multiply', 'RADIO1', key='multiply'), sg.Radio('Divide', 'RADIO1', key='divide')],
        [sg.Frame('Inputs', [
            [sg.Text('Enter the first number:'), sg.InputText(key='first')],
            [sg.Text('Enter the second number:'), sg.InputText(key='second')]])],
        [sg.Button('Submit')]
    ]

    # Create the math_operations window
    window = sg.Window('APP CALCULATOR', layout)

    # WHILE Start a loop until user choose to exit
    while True:
        event, values = window.read()
        if event is (None):
            break

        # TRY calling math operations
        if values is not None and 'first' in values and 'second' in values:
            try:
                num1 = float(values['first'])
                num2 = float(values['second'])
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
                    continue

                # Create Pop-Up to display result
                sg.popup(f'The result is: {result}', title='Result', button_type=sg.POPUP_BUTTONS_OK, keep_on_top=True)
                try_again()
            # exception for ZeroDivisionError using Pop-up
            except ValueError:
                sg.popup('Invalid input. Please enter valid numbers.', title='Math Operation Error', keep_on_top=True)
                try_again()
                break
            # exception for ValueError using Pop-up
            except ZeroDivisionError:
                sg.popup("Cannot divide by zero. Please enter a different second number.", title=" Zero Division Error", keep_on_top=True)
                try_again()
                break

def try_again():
    # Define the try_again window's contents
    layout_try_again = [
        [sg.Text('Do you want to try again?')],
        [sg.Button('Yes'), sg.Button('No')]
    ]            
    # Display try_again window
    window_try_again = sg.Window('Try Again', layout_try_again)
    event = window_try_again.read()
    if event == 'Yes':
        main()
    if event == None or event == 'No':
        sg.popup('Thank you!', title='Exit')
        window_try_again.close()
        exit()

if __name__ == '__main__':
    main()
