import copy
import numpy_lib as np

# Original dataset: a list of image arrays
original_images = [np.random.rand(3, 3) for _ in range(3)]

# Deep copy to preserve original data
augmented_images = copy.deepcopy(original_images)

# Apply transformations to the augmented data
augmented_images[0] = augmented_images[0] * 255  # Simulating scaling

print("Original Images Unchanged:")
print(original_images[0])
print("\nAugmented Images Modified:")
print(augmented_images[0])
