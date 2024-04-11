'''
Implement a program that reads a CSV file named "data.csv," containing columns "Name" and "Age."
Create a new CSV file called "adults.csv" with only the rows of individuals who are 18 years or older.
'''

def process_csv(fname, header=True):
    '''
    Function to filter csv file based on age and create new csv.
    Args:
        fname: Name of csv file to open
    '''
    with open(fname, 'r') as f1, open('adults.csv', 'w') as f2:
        if header:
            head = f1.readline()
            f2.write(head)
        for row in f1:
            try:
                name, age = row.strip().split(',')
                if int(age) >= 18:
                    f2.write(f'{name},{age}\n')
            except ValueError:
                print('Invalid data values.')

    print('Output written to adults.csv')

if __name__=='__main__':
    #take user input
    fname = input("Enter file name: ")
    process_csv(fname)
