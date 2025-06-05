import copy

# Original nested list
original = [[1, 2, 3], [4, 5, 6]]

shallow_copied = original.copy()

# Shallow Copy
# shallow_copied = copy.copy(original)
shallow_copied[0][0] = 100  # Modifying nested data in the copy
print("Shallow Copy Affects Original:")
print("Original:", original)  # The change affects the original list
print("Shallow Copy:", shallow_copied)

# # Reset original
original = [[1, 2, 3], [4, 5, 6]]

# # Deep Copy
deep_copied = copy.deepcopy(original)
deep_copied[0][0] = 100  # Modifying nested data in the copy
print("\nDeep Copy Does Not Affect Original:")
print("Original:", original)  # The original list remains unchanged
print("Deep Copy:", deep_copied)
