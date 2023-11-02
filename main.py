import numpy as np
import matplotlib.pyplot as plt
import time

arr = np.linspace(1, 100, 100)

np.random.shuffle(arr)
import time

# function for bubble sort and plotting
# function for bubble sort and plotting
def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    accesses = 0
    
    for i in range(n):
        for j in range(0, n-i-1):
            
            # color array, default is black
            colors = ['black' for _ in range(len(arr))]
            
            # check if swapping is needed
            swap_needed = arr[j] > arr[j+1]
            
            # update comparison and access counters
            comparisons += 1
            accesses += 2
            
            if swap_needed:
                # set color for the number being swapped
                colors[j] = 'red'
                
                # perform the swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
                # update access counter for the swap
                accesses += 2
            
            # plot the array
            plt.bar(range(len(arr)), arr, color=colors)
            plt.yticks(range(0, int(max(arr)) + 1, 10))
            plt.gca().set_facecolor('white')
            
            # add stats text
            #plt.text(0, max(arr) + 2, f'Comparisons: {comparisons}', fontsize=8, ha='left')
            #plt.text(50, max(arr) + 2, f'Array Accesses: {accesses}', fontsize=8, ha='left')

            
            # save the plot
            plt.savefig(f'photos/{i*n+j+1}.png')
            
            plt.close()

# execute bubble sort
#bubble_sort(arr)
import cv2

# Number of images to convert into video
n = 9801  # Replace this with your actual n value

# setting video dimensions based on first image
image = cv2.imread('photos/1.png')
height, width, layers = image.shape

# initiate video writer
video = cv2.VideoWriter('sorted_array_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 1000, (width, height))

# loop through all saved images
for i in range(1, n + 1):
    img_path = f'photos/{i}.png'
    img = cv2.imread(img_path)
    video.write(img)

# release the video writer
cv2.destroyAllWindows()
video.release()
