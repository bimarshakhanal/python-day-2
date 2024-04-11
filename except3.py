'''
Write a Python program that takes a user input and converts it to an integer.Handle the
ValueError and display a custom error message when the input cannot be converted to an integer.
'''

def convert_input(inp):
    '''
    Function to display content of file
    Args:
        inp: User input
    '''

    try:
         print("Input Converted: ",int(inp))
    except ValueError:
        print("Error: Input cannot be converted to integer.")
    
if __name__=='__main__':
    #take user input
    inp = input("Enter a number: ")
    convert_input(inp)
