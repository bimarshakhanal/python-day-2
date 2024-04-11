'''
Create a function search_log that takes a log file and a search keyword as input. The function
should find and display all lines containing the search keyword.
'''

def process_csv(fname, keyword):
    '''
    Function to search and filter log file using keyword.
    Args:
        fname: Name of log file to open
        keyword: Keyword to search in logfile
    '''
    try:
        with open(fname, 'r') as log:
            for line in log:
                if keyword.lower() in line.lower():  # Case-insensitive search
                    print(line.strip())
    except FileNotFoundError:
        print('Error: Failed to open log file.')


if __name__=='__main__':
    #take user input
    fname = input("Enter file name: ")
    keyword = input("Enter keyword to search: ")
    process_csv(fname,keyword)