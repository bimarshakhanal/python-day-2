'''
Write a Python program that takes two integers as input and performs division (num1 / num2). Handle 
both ValueError (if non-integer input) and ZeroDivisionError and display appropriate error messages.
'''

def safe_division(a,b):
    '''
    Function to display content of file
    Args:
        a: First number
        b: Second number
    '''

    try:
         print("Result: ",int(a)/int(b))
    except ValueError:
        print("Error: Both input should be a number.")
    except ZeroDivisionError:
        print("Error: Second number should not be zero.")
    
if __name__=='__main__':
    #take user input
    a = input("Enter first number: ")
    b = input("Enter second number: ")

    safe_division(a,b)
