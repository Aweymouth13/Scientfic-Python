import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Create a dataset with one dominant component
np.random.seed(0)
data = np.random.randn(100, 2)
data[:, 0] *= 3  # Amplify the first component

# Fit PCA
pca = PCA(n_components=2)
pca.fit(data)

# Transform the data
transformed_data = pca.transform(data)

# Plot the original and transformed data
plt.subplot(1, 2, 1)
plt.scatter(data[:, 0], data[:, 1])
plt.title('Original Data')

plt.subplot(1, 2, 2)
plt.scatter(transformed_data[:, 0], transformed_data[:, 1])
plt.title('Transformed Data (PCA)')

plt.tight_layout()
plt.show()

# Print explained variance ratios
explained_variance = pca.explained_variance_ratio_
print("Explained Variance Ratios:", explained_variance)
