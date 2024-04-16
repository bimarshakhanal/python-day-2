'''
Create a function search_log that takes a log file and a search keyword as input. The function
should find and display all lines containing the search keyword.
'''
import logging

logging.basicConfig(filename='example.log',
                    encoding='utf-8', level=logging.DEBUG)


def process_csv(filename, search_term):
    '''
    Function to search and filter log file using search_term.
    Args:
        fname: Name of log file to open
        search_term: Keyword to search in logfile
    '''
    try:
        with open(filename, 'r', encoding='utf-8') as log:
            for line in log:
                if search_term.lower() in line.lower():  # Case-insensitive search
                    print(line.strip())
    except FileNotFoundError:
        logging.error('Failed to open log file.')


if __name__ == '__main__':
    # take user input
    fname = input("Enter file name: ")
    keyword = input("Enter keyword to search: ")
    process_csv(fname, keyword)
