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
        # Set Text that prompts user to choose from four math operations
        # Set Radio for Addition, Subtraction, Multiplication and Division

        # Create a frame
        # Set text that prompts user to enter the first number by input text
        # Set text that prompts user to enter the second number by input text
        # Set "calculate" button

    # Create the math_operations window
    # Close the math_operations window

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