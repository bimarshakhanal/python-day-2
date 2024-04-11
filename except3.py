'''
Write a Python program that takes a user input and converts it to an integer.Handle the
ValueError and display a custom error message when the input cannot be converted to an integer.
'''
import logging

def convert_input(inp):
    '''
    Function to display content of file
    Args:
        inp: User input
    '''

    try:
         logging.info("Input Converted: ",int(inp))
    except ValueError:
        logging.error("Input cannot be converted to integer.")
    
if __name__=='__main__':
    #take user input
    inp = input("Enter a number: ")
    convert_input(inp)
