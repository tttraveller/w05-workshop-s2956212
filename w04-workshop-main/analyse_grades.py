import numpy as np

def read_grades_data(data_file):
    '''
    Reads data from a text file called `data_file` into a Numpy array.
    '''
    # Create a Numpy array from the data in the file
    all_grades = np.loadtxt(data_file,delimiter=',')

    # Return the Numpy array
    return all_grades
#explore the data
def EDA(all_grades):
    average = np.mean(all_grades,axis=0)
    median = np.median(all_grades,axis=0)
    quartile = np.percentile(all_grades,[25,50,75],axis=0)
    std = np.std(all_grades,axis=0)
    return average,median,quartile,std

# ---
# Analysis of the grades data

# Get the data from the file
all_grades = read_grades_data('grades.txt')
print(all_grades[:5,])
print(EDA(all_grades))

