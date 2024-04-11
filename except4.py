'''
Write a Python program that takes two integers as input and performs division (num1 / num2). Handle 
both ValueError (if non-integer input) and ZeroDivisionError and display appropriate error messages.
'''

import logging

def safe_division(a,b):
    '''
    Function to perform safe division - handle division by zero
    Args:
        a: First number
        b: Second number
    '''

    try:
         print("Result: ",int(a)/int(b))
    except ValueError:
        logging.error("Both input should be a number.")
    except ZeroDivisionError:
        logging.error("Second number should not be zero.")
    
if __name__=='__main__':
    #take user input
    a = input("Enter first number: ")
    b = input("Enter second number: ")

    safe_division(a,b)
