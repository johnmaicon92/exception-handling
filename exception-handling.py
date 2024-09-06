"""
1. Exceptional Weather Forecast
Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a weather forecast application that gracefully handles unexpected user input and provides user-friendly error messages.

Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.
"""

fahrenheit = int(input("Please enter the temperature in Fahrenheit: "))

"""Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.

Use a try block to catch any potential errors during the conversion process. What happens if they type out "thirty" instead of doing 30?
"""

def fahrenheit_to_celsius():
    fahrenheit = int(input("Please enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
   
fahrenheit_to_celsius()

"""Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 

Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."


Task 4: Finally Add a finally block that thanks the user for using the weather forecast application, ensuring that this message is displayed regardless of whether an exception was caught or not.

NOTE: Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs.
"""

def fahrenheit_to_celsius():
    fahrenheit = int(input("Please enter the temperature in Fahrenheit: "))

    try:
        celsius = (fahrenheit - 32) * 5/9
        print(f"The temperature in Celsius is {celsius:.1f}")

    except ZeroDivisionError:
        print("Can not divide by zero")

    except OverflowError:
        print("Overflow error")

    except ValueError:
        print("Something went wrong. Please enter a valid number.")

    else:
        print(f"{fahrenheit}° Fahrenheit is equal to {celsius:.1f}° Celsius!")

    finally:
            print("Thank you for using the weather forecast application!")

    return celsius
   


def celsius_to_fahrenheit():
    celsius = int(input("Please enter the temperature in Celsius: "))

    try:
        fahrenheit = (celsius * 9/5) + 32
        print(f"The temperature in Fahrenheit is {fahrenheit:.1f}")

    except ZeroDivisionError:
        print("Can not divide by zero")

    except OverflowError:
        print("Overflow error")

    except ValueError:
        print("Something went wrong. Please enter a valid number.")

    else:
        print(f"{celsius}° Celsius is equal to {fahrenheit:.1f}° Fahrenheit!")

    finally:
            print("Thank you for using the weather forecast application!")

    return fahrenheit
   

while True:
    welcome = input("Hello there! The Temperature you want to convert is in Celsius or Fahrenheit? (C)/(F): ").upper().strip()
    if welcome == "C":
        celsius_to_fahrenheit()
    elif welcome == "F":
     fahrenheit_to_celsius()
    break