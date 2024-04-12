'''
Write a Python program that takes two integers as input and performs division (num1 / num2).
Handle the ZeroDivisionError and display a custom error message when the second number is zero.
'''

import logging

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

def safe_division(a,b):
    '''Function to divide two numbers with zero division exception check.'''
    try:
        logging.info('Division sucessful.')
        return a/b
    except ZeroDivisionError:
        logging.error("Second number cannot be zero.")
        return None
    
if __name__=='__main__':
    #take user input
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print('Result: ', safe_division(a,b))
