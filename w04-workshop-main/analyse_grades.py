import numpy as np
import matplotlib.pyplot as plt


# Task 1: Read the data
def read_grades_data(data_file):
    '''
    Reads data from a text file into a NumPy array.
    '''
    all_grades = np.loadtxt(data_file, delimiter=',')
    return all_grades


# Task 2: Explore the data
def EDA(all_grades):
    average = np.mean(all_grades, axis=0)
    median = np.median(all_grades, axis=0)
    quartile = np.percentile(all_grades, [25, 50, 75], axis=0)
    std = np.std(all_grades, axis=0)

    avg_stu = np.mean(all_grades, axis=1)

    # Calculate the class statistics for overall course grades
    avg_course = np.mean(avg_stu)
    std_course = np.std(avg_stu)

    return average, median, quartile, std, avg_course, std_course


# Task 3: Plot histograms
def grade_histograms(all_grades):
    fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

    bins = np.arange(0, 101, 10)

    for i in range(4):
        axs.flat[i].hist(
            all_grades[:, i],
            bins=bins,
            color='skyblue',
            edgecolor='black'
        )

        axs.flat[i].set_title(f'Assignment {i + 1}')
        axs.flat[i].set_xlabel('Grade')
        axs.flat[i].set_ylabel('Number of students')
        axs.flat[i].set_xlim(0, 100)

    plt.tight_layout()
    plt.show()


# Main program
all_grades = read_grades_data('grades.txt'
)
print(all_grades[:5, :])
average, median, quartile, std, avg_course, std_course = EDA(all_grades)
print("Average grades:", average)
print("Median grades:", median)
print("Quartiles:", quartile)
print("Standard deviations:", std)
print("Overall course average:", avg_course)
print("Overall course standard deviation:", std_course)
grade_histograms(all_grades)