#reconstruction file
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.image import imread
from PIL import Image
import os

#list files in directory
print(os.listdir())



# function to add salt and pepper noise
def sp_noise(image, prob):
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = np.random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

# function to reconstruct image with k singular values
def reconstruct_image(s, u, vt, k):
    sigma = np.diag(s[:k])
    x_ap = np.dot(u[:, :k], sigma).dot(vt[:k, :])
    return x_ap

# read the original image and calculate the svd
a = imread('photo.jpeg')
x = np.mean(a, -1)
u, s, vt = np.linalg.svd(x, full_matrices=False)

# list of k values and their respective relative sizes
k_values = [1, 5, 50, 500, 'OG', 1200]
relative_sizes = [(u[:, :k].nbytes + s[:k].nbytes + vt[:k, :].nbytes) / x.nbytes * 100 if k != 'OG' else 100 for k in k_values]

# create a subplot to display images for different k values including the original image
fig, axes = plt.subplots(1, len(k_values), figsize=(24, 4))

# loop through each k value and display the reconstructed image
for i, k in enumerate(k_values):
    if k == 'OG':
        # display the original image
        axes[i].imshow(x, cmap='gray')
        axes[i].set_title(f'og\n{relative_sizes[i]:.2f}% og size')
    else:
        # reconstruct the image with k singular values
        x_ap = reconstruct_image(s, u, vt, k)
        # display the reconstructed image
        axes[i].imshow(x_ap, cmap='gray')
        axes[i].set_title(f'k = {k}\n{relative_sizes[i]:.2f}% og size')
    
    axes[i].axis('off')

# save the subplot as a downloadable file
plt.savefig('svd_reconstructed_images_with_og.png')
plt.show()
