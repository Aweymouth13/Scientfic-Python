# For this week, the required libraries to run locally are `astropy` and `numpy`.

**Exercise 1: Objective**

Given cities, country abbreviations, skyscrapers, and heights, create a `for` loop that prints to certain specifications.

1. Defined the dictionaries.
2. Used `astropy` to get a conversion factor from given feet to requested AUs.
3. Loop through each parameter and include a print statement to display the requested output.


**Exercise 2**

We are asked to work with a mixed dtype list

1. I created a list named `list_2` with required elements.
2. Checked and printed the data types of the elements in the list.
3. Removed the element `3.1` from the list and confirmed its removal.
4. Appended Euler's gamma constant (`np.euler_gamma`) to the list and confirmed its addition.
5. I repeated the list 3 times.
6. Printed each individual element in the list multiplied by 3.
7. Achieved the same result as the previous step but using a `for` loop and a separate list named `new_list`.


**Exercise 3**

Given an array `a` we are asked to produce specific outputs.

1. Initialized the array.
2. Created a variable for each slice.
3. For the first variable, I sliced by every other element, for the second every 3rd, 4th, and 5th element, for the third I reversed.
4. Printed the results to console.


**Exercise 4**

Converting an array and using boolean slicing to print requested outputs.

1. Converted to a Numpy array.
2. Printed out the old array `a` and the new `a_np` along with their dtypes for confirmation.
3. Set conditional format for when an element of the array is greater than 5.
4. Set a second conditional format for when an element of the array is greater than 5 or equal to 2.

**Exercise 5**

Considering a list for an inferior TV show and zipping lists in a for loop.

1. Initialized lists for `episodes`, `line`, and `seasons`.
2. Used zip to iterate through multiple lines of the list.
3. Decided to do extra work because my favorite fantasy show was not part of the lists.
4. Made an early 2000's infomercial reference.
5. Created new lists for LOTR.
6. Iterated through the list of the superior show.

**Exercise 6**

Build upon example 3 from in class to enumerate indexed lists.

1. Initialized lists.
2. Created an empty array to hold absolute magnitude.
3. Checked the dimensions to ensure they are the same, in this case (4).
4. Loop through each of the stars and print the absolute magnitude in the required format.
5. Printed the full array of absolute magnitude, noticing that it isn't formatted well.


**Exercise 7**

Given a list of vals, create another list with conditional filtering.

1. Initialize vals.
2. Create another list called `vals2`.
3. For an element x and the corresponding i in vals, check if 1/x > 1/x^2.
4. Return the value *3 if that condition is true and add it to vals2.
5. Vals2 is printed.

**Exercise 8**

Use the numpy generation function to generate a random array, make a second array to change the 0th column.

1. Assign m x n size.
2. Create a random integer array of size m x n (in this case random between 0 and 100 of size 4x3).
3. Print the array `multi_array`.
4. Use np.copy to copy to a new array `multi_array_2`.
5. Slice the array `[:,0] = 1` to change the array such that the 0th column is replaced by 1.
6. Display both arrays.

**Exercise 9**

Given a data file `spectrum_oct17_adi.dat`, replace certain values in the "uncertainty" column where the SNR is less than 5.

1. Use `np.loadtxt` to read in the data into a variable called `df`.
2. Separate out the columns for "wavelength," "flux_density," "uncertainty," and "SNR."
3. Use `np.where` to find indices where the SNR is less than 5.
4. Replace those values in the "uncertainty" column with -9.
5. Save the cleaned-up data to a new text file.


**Exercise 10**

Generate an array using `np.linspace`, reshape it, and perform various transformations.

1. Create a new array with `np.linspace` of 100 elements between 5 and 10.
2. Convert it to a column vector using `reshape`.
3. Reshape it to a 2D array with 20 rows.
4. Transpose the array.
5. Flatten the transposed array back to 1D.



**Exercise 11**

Use `np.genfromtxt` to read in data from a CSV, clean up entries, and perform condition-based calculations.

1. Read in the data from `test.csv` with `np.genfromtxt`, skip the first 36 rows.
2. Identify the columns for "semimajor_axis" and "discovery_method."
3. Replace empty entries in the "semimajor_axis" column with -1.
4. Convert the "semimajor_axis" to floats with `astype`.
5. Use `np.where` to find relevant entries based on discovery methods.
6. Calculate and print the median semimajor_axis for each discovery method.
7. Save the cleaned data to a new CSV file with `np.savetxt`.



