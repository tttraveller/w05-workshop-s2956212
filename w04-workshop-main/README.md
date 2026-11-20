# Week 4 workshop - NumPy arrays and plotting

The file `grades.txt` contains the grades (out of 100) obtained by 300 students on a course, on 4 different assignments. Your task this week is to read this data into a NumPy array, to plot some useful visualisations, and to report some interesting statistics about the class. You will write functions to separate the different sub-tasks, which you will then call to produce your results.

This is our first workshop working with NumPy arrays. For certain tasks, you will need to select different rows, columns, or specific values in an array depending on a condition; the examples on indexing and slicing from the `11_numpy.ipynb` notebook which you've seen this week should be useful.

As usual, the **driver** starts by creating the team repo on GitHub from the template, giving access to their navigator(s), and cloning the repo into Noteable. Don't forget to **switch roles every 15 minutes or so**, or whenever you complete a sub-task if that feels more natural. **Each of you must take on the driver role at least once during the workshop.**

This week, you will need to consult the documentation to find out how to do some of the tasks -- this is a great job for the **navigator**.

## Task 1: read the data into a NumPy array

Your first job is to read the data from the file `grades.txt` into a NumPy array. To do this, we can actually use one of NumPy's functions, `np.loadtxt`, which can load data from `.txt` plain text files.

There are already some starter code in `analyse_grades.py`, but if you try to run it, you'll see an error. Debug it together! Here are some clues:

- Look inside the `grades.txt` file. What does the data look like?
- Read the error trace. What is the type of the error? What does the error message suggest?
- Look at the [documentation for the `np.loadtxt` function](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html?highlight=loadtxt#numpy.loadtxt). What does it expect the data will look like? Does this match what your data looks like? Is there something you can use there to solve the problem?

When you think you've fixed the problem, print out the first few rows of the `all_grades` array to check that this matches the data in `grades.txt`.

## Task 2: exploring the data

Have a look at [NumPy's statistics functions](https://numpy.org/doc/stable/reference/routines.statistics.html), and compute some useful statistics for your class. Below are some suggestions to get started -- but feel free to explore more questions. In some cases, you will need the statistics functions (or other Numpy functions -- explore the documentation!); in other cases, you will need to select values from the array based on a condition.

Consider how you will structure your code into different small functions to answer these questions. Here is a suggestion -- but if you have a different idea, you should try it!

1. What is the average grade and the standard deviation for each of the 4 assignments?
2. What is the median grade, first quantile (25th percentile), and third quantile (75th percentile) for each of the 4 assignments?
3. Assuming each assignment counts equally for 25% of a student's grade, what is the average course grade and the standard deviation for the class?

For the first question, you will need to be able to calculate an average and standard deviation over one column of the array. For the third question, you will also need to calculate the average and standard deviation, but this time over one row.

- You can write a function to do this calculation, given a 1-dimensional Numpy vector (which could be either a row or a column), and return the average and standard deviation, calculated with the help of Numpy statistics functions. Let's call it `average_std()`.
- You can then write another function, say `course_stats()`, which takes a Numpy array as input with all the grades, and calls `average_std()` inside on each of the columns, one at a time, to give the results for each assignment.
- For the second question, you can write another function `quartiles()` to return the 3 quartiles for one given assignment. Then, you could modify your `course_stats()` function to also calculate and return the quartiles for all 4 assignments, by calling your `quartiles()` function each time.
- For the third question, you can either write a new function just for returning the overall course grade and standard deviation, or you could also incorporate this in your `course_stats()` function.

You will need to think carefully about what is the best way to return your results (separate values, as a list, something else...).

Once you have functions to answer all the questions, call them at the end of your script, and display the results on the screen in a way that is easy to read. You can use **f-strings** ([documentation](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings)) to format your results and make the report more readable. For example, if you've stored the average grades for each assignment in a list or an array `averages`, you could create a string to display:

```python
average_report = f'The average grade for Assignment 1 was {averages[0]:.1f}.\n'
average_report += f'The average grade for Assignment 2 was {averages[1]:.1f}.\n'
...
print(average_report)
```

Note that you could also create your display strings using a loop. You can also put your display code in a function.

## Task 3: make some plots!

### Note: Plotting in Noteable

In Jupyter notebooks, you have used `plt.show()` after creating a plot, to actually display it below the code cell. But unfortunately, `plt.show()` may not work from a `.py` script ran on Noteable.

If you have this problem, there is a workaround:

1. Right-click anywhere in the code editor (where you type code) with your `.py` script open.
2. Select "Run in interactive window".
3. If the only option is "Install the Jupyter extension", do this (this should only show up once), then go back to step 1 after it's installed. It should only take a few seconds.
4. Select "Run current file in interactive window".

This will open another window to the right, which is essentially a temporary Jupyter notebook; in particular, `plt.show()` will work as expected, and you should see your plot appear in that window.

You can also select "Run current file in interactive window" from the little drop-down menu right next to the "Run" button.

### Visualising grade distributions

You have all the grades in a NumPy array, with each row corresponding to a student and each column to an assignment. To get a general view of the class' results, for example, we could plot some histograms. A histogram will display the distribution of grades, with the grades on the x-axis, and the number of students who got each grade on the y-axis. You can also create histograms where each bar represents a range of grades, rather than a single grade (for example, you could divide grades from 0 to 100 into 20 "bins", with the first bar counting all students who got between 0 and 4, the second bar counting students who got between 5 and 9, the third bar between 10 and 14, etc...)

- Search the `matplotlib` documentation to find out how to plot histograms -- it's available at [matplotlib.org](https://matplotlib.org/). You can use your favourite search engine to search the documentation -- for example, you could search Google for `histogram site:matplotlib.org`.
- Plot a histogram of the grades for **each** assignment (each column in the data). This will tell you how many students in the class got a certain grade, for all 4 assignments.
    - You will need to produce 4 histograms. Search for "subplot" in the documentation for how to do this.
    - Your bins (the x-axis) should start at 0 and end at 100.
    - You could choose to plot this either by grade band (that is, every bin has width 10, for example group students who got between 60 and 69) or by individual grade (one bin per integer between 0 and 100).

Put your plotting code in a function, called `grade_histograms()`, which takes the `all_grades` array as input, and doesn't return anything, but plots and displays the four histograms. Call your function to produce the plots at the end of your script.


## Extra practice questions, if you still have time (if not: do them at home!)

- Find a way to display the 4 histograms on 1 graph, with 4 different bars for each bin, each bar with a different colour. Add a legend to indicate which colour corresponds to which assignment.

- If you can think of other ways to display this data, which would give you more information, try it! (matplotlib can do boxplots, for example.)

- In each assignment, how many students got an A (grade 70 or greater)? How many students got an A for **all 4 assignments**?

- How many students have passed the course (grade 50 or greater overall)? How many students got a distinction (grade 70 or higher)? How many students will be allowed to take a resit exam (grade between 30 and 49)?

- How would the results change if the weights of each assignment were different? Adapt your function(s) to be able to (optionally) calculate weighted averages, with the weights given as an extra input, and experiment with different values. Remember that the weights need to sum to 100%. If no weights are provided, the default behaviour should be that all assignments count for the same weight.

- There was a zombie apocalypse at the end of the semester, and some of the students turned into zombies -- their work for Assignment 4 may not have been their best. To compensate for this, the University put in place a "no detriment" policy for Assignment 4. Starting from their pre-zombie-apocalypse grade (weighted average of the first 3 assignments, weights 10%, 25%, and 15% respectively, but scaled up to sum to 100% overall):
    - if their grade for Assignment 4 improves their total grade for the course, then Assignment 4 counts as normal (with 50% weight).
    - if their grade for Assignment 4 decreases their total grade for the course, then Assignment 4 is discounted, and the student's grade for the course is their grade pre-apocalypse.

Calculate the final course grades for all students, taking into account the "no detriment" policy. How many students passed the course before the policy was applied? How many students passed after?

It's possible to do this without looping over all the students, using operations on Numpy arrays -- try it!
