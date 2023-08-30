"""
Week 2 Homework Set: Aaron Weymouth, KTX887
I'm unsure about the 'explaination of how it is run'. I will comment all part of the code that I can
and give a blub in the readme.txt file. I've also tried to interpret the homework as well as I can!

I'm only taking two classes this semester and my other one is a breeze, I'll be devoting many hours a week
to this class :)

I am a BI analyst for my job, I use python analytics every day. I am trying to take my knowledge and apply
it to Physics/Astronomy. I'm always open to feedback on my code!

In some exercises I have used additonal libraries for a challange
"""

######### You can also access at this link! This is a shared site and will contain all work up-to-date #########
# https://app.noteable.io/f/b1b7999c-7e05-495e-bda9-ef6bc2919151/Week-2-Assignments.ipynb

from astropy import units as u
import numpy as np

#Exercise 1
#Given cities, country abbreviations, skyscraper and their heights, for loop that prints out in a specfic format


#define dictonaries
city_to_country = {'Paris': 'FR', 'New York': 'USA', 'Kuala Lumpur': 'MY'}
country_to_building = {'FR': 'Eiffel Tower', 'USA': 'WTC', 'MY': 'Petronas Towers'}
building_to_height = {'Eiffel Tower': 1083, 'WTC': 1776, 'Petronas Towers': 1483}

#use astropy for practice
ft_to_au = (u.imperial.ft).to(u.au)
print(ft_to_au, 'feet per AU')

#loop thru dict
for city, country_abb in city_to_country.items():
    building = country_to_building[country_abb]
    height_ft = building_to_height[building]
    height_au = height_ft * ft_to_au
    print(f'The tallest building in the city of {city}, {country_abb} is the {building} with a height of {height_au:.3e} au')

#Exercise 2
#start with a mixed list, remove, append, repeat, prints in different ways
print('--' * 10)
print('Exercise 2')
list_2 = [np.pi, np.e, 3.1, 5]

#checking dtypes
print('the data types in order are :', [type(i) for i in list_2])

#remove 3.1
list_2.remove(3.1)
if 3.1 not in list_2:
    print('3.1 has been removed')

#append eulers gamma constant
list_2.append(np.euler_gamma)
if np.euler_gamma in list_2:
    print('eulers gamma constant has been added')

#repeates the list 3 times, doesn't work with dictionaries tho
print('here is the list 3 times! ', list_2 * 3)

#prints each indvidual element of the list * 3
print('here is each element in the list multiplied by 3 : ', [i * 3 for i in list_2])

#same as above, but with a for loop
new_list = [] #for formatting to look like above line
for i in list_2:
    new_list.append(i * 3)
print('here is each element in the list multiplied by 3 : ', new_list)



#Exercise 3
#given an array given, produce specfic outputs
print('--' * 10)
print('Exercise 3')

#given array
a = [2,3,5,6,8,9,10]

#variables for clarity
first_slice = a[::2] #every other element
second_slice = a[3:6] #3rd, 4th, 5th element
third_slice = a[::-1] #reverse

print('the original array : ', a)
print('the first slice : ', first_slice)
print('the second slice : ', second_slice)
print('the third slice : ', third_slice)

#Exercise 4
#converting an array then use conditional/boolian slicing to print out specfic outputs
print('--' * 10)
print('Exercise 4')

#convert to numpy array
a_np = np.array(a)

#orginal array
print('the original array : ', a, 'with a data type of : ', type(a))
print('the numpy array : ', a_np, 'with a data type of : ', type(a_np))

exercise_4_result = a_np[a_np > 5]
print('the elements greater than 5 : ', exercise_4_result)

# elements greater than 5 or equal to 2
exercise_4_result_2 = a_np[(a_np > 5) | (a_np == 2)]
print('the elements greater than 5 or equal to 2: ', exercise_4_result_2)


#Exercise 5
#consider some lists, use zip and for loop to produce desired result
print('--' * 10)
print('Exercise 5')

#given lists
# MST3K lists per assignment, but Lord of the Rings > MST3K. Change my mind.

episode = ['Eegah', 'Deathstalker', 'Space Mutiny']
line = ["Watch out for Snakes", "He's Batman", "Big McLarge Huge"]
season = [5, 7, 8]

#use zip to iterate of multiple lists
for ep, ln, se in zip(episode, line, season):
    print(f'The best line of the episode {ep} in season {se} was "{ln}"')

print('Billy Mays Here but Wait there is more!')

# given lists, now featuring Lord of the Rings because, well, it's just better.
movies = ['Fellowship of the Ring', 'The Two Towers', 'Return of the King']
line2 = ['you shall not pass!', 'PO-TA-TOES!', 'still only counts as one!']
movie_year = [2001, 2002, 2003]

#zip and iterate, just like the fellowship did through middle-earth
for mo, ln, se in zip(movies, line2, movie_year):
    print(f'The best line of the movie {mo} released in {se} was "{ln}"')

#Exercise 6
#use example 3 and also use enumerate to print out the number of the start in an indexed list
print('--' * 10)
print('Exercise 6')

#given in ex 3 datastructures
starname = ['HIP 99770', 'AF Lep', 'HR 8799', 'Vega']
spectype = ['A5V', 'F8V', 'F0V', 'A0V']
starmag = np.array([4.9, 6.3, 5.9, 0.0])
dstar = np.array([40.74, 26.8, 39.4, 7.7])

#empty np array for absmag
absmag_array = np.zeros(len(starname))

#dim checking
if len(starname) == len(absmag_array):
    print('the arrays are the same length (', len(starname), ') no errors.')
else:
    print('the arrays have different lengths. I failed this exercise.')


#loop thru each star and print out the absmag
for idx, (i, j, k, l) in enumerate(zip(starname, spectype, starmag, dstar)):
    absmag = k - 5 * np.log10(l / 10.)
    absmag_array[idx] = absmag  # store the value in the array
    print(f'The absolute magnitude of star number {idx+1} with name {i} with spectral type {j} is {absmag:.3f}')

#print the full array of absmag
print(absmag_array)


#Exercise 7
#create vals2 by multiplying elements of vals by 3 if 1/x is greater than 1/x^2
print('--' * 10)
print('Exercise 7')


vals = [.1, 2, .4, 3]
vals2 = [int(vals[i] * 3) for i, x in enumerate(vals) if 1/x > 1/x**2]
print('The elements that meet the condition are : ', vals2)


#Exercise 8
#numpy to generate array m x n and another array with some adjustments to 0th column
#will use integer array for simplicity
print('--' * 10)
print('Exercise 8')

#random number array
m = 4
n = 3

#generate m x n rand array
multi_array = np.random.randint(0, 101, size=(m, n))
#prints random array of size m x n is size
print('the random array', 'of size', m, 'x', n, 'is :\n', multi_array)

#creates multi_array2 with 0th column of multi_array
multi_array_2 = np.copy(multi_array)
multi_array_2[:,0] = 1
print('the new array with 0th column of multi_array set to 1 is :\n', multi_array_2)



#Exercise 9
#read in file spectrum... using np.loadtxt, use np.where to replace certain values by -9
print('--' * 10)
print('Exercise 9')

#read in file with np.loadtxt
df = np.loadtxt('spectrum_oct17_adi.dat')
print('data from the file has been loaded into df')

#columns for wavelength, flux density, uncertainty, and SNR
wavelength = df[:,0] #all rows, 0th column
flux_density = df[:,1] #all rows, 1st column
uncertainty = df[:,2] #all rows, 2nd column
SNR = df[:,3] #all rows, 3rd column

#replace values where SNR < 5 with -9
indicies = np.where(SNR < 5)
uncertainty[indicies] = -9

#saves to a new file, will be called ex9 output for this purpose
updated = np.column_stack((wavelength, flux_density, uncertainty, SNR))
np.savetxt('ex9_output.txt', updated, fmt='%1.3f', delimiter=' ', header='wavelength flux_density uncertainty SNR')
print('the new file has been saved as ex9_output.txt sucessfully!')
print('it looks like this : \n', updated)
print('wow much negative 9s!')


#Example 10
#asked to use linspace to create an array, convert it to a row vector or column vector, transpose, then flatten
print('--' * 10)
print('Exercise 10')

#new array w/ linspace
da_array = np.linspace(5, 10, num=100)
#array shape
print(f'the shape is : {da_array.shape}')


#col vector w/ reshape
col_vec = da_array.reshape(-1, 1)
print(f'the shape of the col vector is : {col_vec.shape})')
      

#2d array w/ reshape
two_d_array = col_vec.reshape(20, -1)
print(f'the shape of the 2d array is : {two_d_array.shape})')

#da array transposed
trans_array = two_d_array.transpose()
print(f'the shape of the transposed array is : {trans_array.shape})')

#flatten it backkkk
flat_array = trans_array.flatten()
print(f'the shape of the flattened array is : {flat_array.shape})')


#Exercise 11
#without looping, clean entries etc: use np.where after cleaning, astype to floating points

print('--' * 10)
print('Exercise 11')

#read in data and skip first 36 rows
data = np.genfromtxt('test.csv',dtype=str, delimiter=',', skip_header=35)
print('the data has been read in and it looks like', data)

#pl_orbsmax and discoverymethod columns
semimajor_axis = data[1:,6]
discovery_method = data[1:,4]

#replace empty entries with -1
semimajor_axis[semimajor_axis == ''] = -1

#convert to float
semimajor_axis = semimajor_axis.astype(float)

#use np.where over a for loop for some reason, i'm not sure if this works
index_4_imaging = np.where((discovery_method == 'Imaging') & (semimajor_axis >= 0))
index_4_radial = np.where((discovery_method == 'Radial Velocity') & (semimajor_axis >= 0))
index_4_transit = np.where((discovery_method == 'Transit') & (semimajor_axis >= 0))

median_imaging = np.median(semimajor_axis[index_4_imaging]) if index_4_imaging[0].size else "No Data"
median_radial = np.median(semimajor_axis[index_4_radial]) if index_4_radial[0].size else "No Data"
median_transit = np.median(semimajor_axis[index_4_transit]) if index_4_transit[0].size else "No Data"

print(f"Median for Imaging: {median_imaging}")
print(f"Median for Radial Velocity: {median_radial}")
print(f"Median for Transit: {median_transit}")

#export to example 11 output

np.savetxt('ex11_output.csv', data, delimiter=',', fmt='%s')


#https://stackoverflow.com/questions/47699023/how-to-write-console-output-on-text-file
