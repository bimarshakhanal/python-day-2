'''
Write a Python program that takes a user input and converts it to an integer.Handle the
ValueError and display a custom error message when the input cannot be converted to an integer.
'''
import logging

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)

def convert_input(inp):
    '''
    Function to display content of file
    Args:
        inp: User input
    '''

    try:
         inp = int(inp)
         logging.info("Input Converted.")
    except ValueError:
        logging.error("Input cannot be converted to integer.")
    
if __name__=='__main__':
    #take user input
    inp = input("Enter a number: ")
    convert_input(inp)
