import numpy as np
"""### 9. NumPy Slicing with Boolean Indexing

Read in file ``spectrum_oct17_adi.dat`` from the notes using ``np.loadtxt``.   It has columns of wavelength, flux density, uncertainty (flux density), and signal-to-noise ratio.   

 Use the ``np.where`` statement to replace the values for uncertainty (flux density) by ``-9`` for rows where the signal-to-noise ratio is less than 5.

Save a new file with columns of wavelength, flux density, uncertainty (flux density), and signal-to-noise ratio, where you have updated the uncertainty values."""

#read in file 
data = np.loadtxt('spectrum_oct17_adi.dat')

#define columns
wavelength = data[:,0]
flux_density = data[:,1]
uncertainty = data[:,2]
snr = data[:,3]

print(data)

#update uncertainty where snr < 5
indices = np.where(snr < 5)
uncertainty[indices] = -9

#save to new document
new_data = np.column_stack((wavelength, flux_density, uncertainty, snr))
print(new_data)
np.savetxt('test', new_data)