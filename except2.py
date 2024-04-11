'''
Implement a program that takes user input for a filename, opens the file in read mode, and displays its
contents. Handle the FileNotFoundError and display an error message if the file is not found.
'''

def read_file(fname):
    '''
    Function to display content of file
    Args:
        fname: Name of file to open
    '''

    try:
         file = open(fname, 'r')
         print('***File content***\n',file.read())
    except FileNotFoundError:
        print("Error: Filename with given name not found.")
    
if __name__=='__main__':
    #take user input
    fname = input("Enter file name: ")
    read_file(fname)
