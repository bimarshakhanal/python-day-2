'''
Write a Python program that takes user input for age. Create a custom exception
InvalidAgeError to handle cases where the age is below 0 or above 120.
'''

class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        self.message = f"Invalid age {age}: Age must be between 0 and 120."
    
    def __str__(self):
        return self.message

def check_age(age):
    if age <0 or age > 120:
        raise InvalidAgeError(age)
  
if __name__=='__main__':
    #take user input
    age = int(input("Enter your age: "))
    try:
        check_age(age)
    except InvalidAgeError as e:
        print(e)
