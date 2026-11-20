import numpy as np

def read_grades_data(data_file):
    '''
    Reads data from a text file called `data_file` into a Numpy array.
    '''
    # Create a Numpy array from the data in the file
    all_grades = np.loadtxt(data_file)

    # Return the Numpy array
    return all_grades



# ---
# Analysis of the grades data

# Get the data from the file
all_grades = read_grades_data('grades.txt')
