'''
Implement a program that takes user input for a filename, opens the file in read mode, and displays
its contents. Handle the FileNotFoundError and display an error message if the file is not found.
'''

import logging

logging.basicConfig(filename='example.log',
                    encoding='utf-8', level=logging.DEBUG)


def read_file(filename):
    '''
    Function to display content of file
    Args:
        filename: Name of file to open
    '''

    try:
        file = open(filename, 'r', encoding='utf-8')
        logging.info(f"File opened,{filename}")
        print('***File content***\n', file.read())
    except FileNotFoundError:
        logging.error("Filename with given name not found.")


if __name__ == '__main__':
    # take user input
    fname = input("Enter file name: ")
    read_file(fname)
