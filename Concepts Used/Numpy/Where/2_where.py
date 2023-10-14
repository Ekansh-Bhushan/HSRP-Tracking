import numpy as np

arr = np.array([1, 2, 3, 4, 5])
condition = (arr > 3)
result = np.where(condition)
print(result)  # Output: (array([3, 4]),), where 3 & 4 represents indices
