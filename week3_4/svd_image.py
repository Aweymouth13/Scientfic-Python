import numpy as np

import matplotlib.pyplot as plt
from matplotlib.image import imread
plt.rcParams['figure.figsize']=[16,8]

def truncate_image(k=5):

 A=imread('thephoto.jpg')

 X=np.mean(A,-1)

 img=plt.imshow(X)
 img.set_cmap('gray')
 plt.axis('off')

 plt.show()

 U,s,VT=np.linalg.svd(X,full_matrices=False)
 Sigma=np.diag(s)


 X_Ap = np.dot(U[:,:k],Sigma[0:k,:k]).dot(VT[:k,:])

 img=plt.imshow(X_Ap)

 img.set_cmap('gray')
 plt.axis('off')
 plt.title('k = '+str(k))
 plt.show()
  #plt.savefig('hubble'+str(k)+'.png')


def denoise_image(k=5,nlevel=0.05,plotme=True):

 #A=imread('cat.jpeg')
 #A=imread('acdc2.jpg')
 #A=imread('pinkfloyd.png')
 #A=imread('noisy.png')
 A=imread('thephoto.jpg')

 A_orig=A.copy()

 A=sp_noise(A,nlevel)
 try:
  X=np.mean(A,-1)
 except:
  X=A

 img=plt.imshow(X)
 img.set_cmap('gray')
 plt.axis('off')

 plt.show()

 U,s,VT=np.linalg.svd(X,full_matrices=False)
 Sigma=np.diag(s)

 if plotme:
  plt.plot(np.arange(0,len(s))+1,s/np.max(s),c='tab:green',marker='o',ms=2)
  plt.yscale('log')
  plt.ylim(np.min(s)/np.max(s),1.01)
  plt.xlabel('Singular Value',size=16)
  plt.ylabel('$\Sigma_{i}/\Sigma_{i,max}$',size=16)
  plt.show()


 X_Ap = np.dot(U[:,:k],Sigma[0:k,:k]).dot(VT[:k,:])

 img=plt.imshow(X_Ap)

 img.set_cmap('gray')
 plt.axis('off')
 plt.title('k = '+str(k))
 plt.show()
  #plt.savefig('hubble'+str(k)+'.png')


def sp_noise(image, prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = image.copy()
    if len(image.shape) == 2:
        black = 0
        white = 255            
    else:
        colorspace = image.shape[2]
        if colorspace == 3:  # RGB
            black = np.array([0, 0, 0], dtype='uint8')
            white = np.array([255, 255, 255], dtype='uint8')
        else:  # RGBA
            black = np.array([0, 0, 0, 255], dtype='uint8')
            white = np.array([255, 255, 255, 255], dtype='uint8')
    probs = np.random.random(output.shape[:2])
    output[probs < (prob / 2)] = black
    output[probs > 1 - (prob / 2)] = white
    return output
  
import os

def list_files_in_directory():
    print(os.listdir())

def reconstruct_image(s, u, vt, k):
    sigma = np.diag(s[:k])
    x_ap = np.dot(u[:, :k], sigma).dot(vt[:k, :])
    return x_ap

def plot_reconstructed_images(image_path, k_values=[1, 5, 50, 500, 'OG', 1200]):
    a = imread(image_path)
    x = np.mean(a, -1)
    u, s, vt = np.linalg.svd(x, full_matrices=False)

    relative_sizes = [(u[:, :k].nbytes + s[:k].nbytes + vt[:k, :].nbytes) / x.nbytes * 100 if k != 'OG' else 100 for k in k_values]

    fig, axes = plt.subplots(1, len(k_values), figsize=(24, 4))

    for i, k in enumerate(k_values):
        if k == 'OG':
            axes[i].imshow(x, cmap='gray')
            axes[i].set_title(f'og\n{relative_sizes[i]:.2f}% og size')
        else:
            x_ap = reconstruct_image(s, u, vt, k)
            axes[i].imshow(x_ap, cmap='gray')
            axes[i].set_title(f'k = {k}\n{relative_sizes[i]:.2f}% og size')
        
        axes[i].axis('off')

    plt.savefig('svd_reconstructed_images_with_og.png')
    plt.show()
