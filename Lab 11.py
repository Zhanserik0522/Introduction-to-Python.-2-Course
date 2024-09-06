import numpy as np

arr = np.array([2, 3, 5, 6, 1, 2, 4])

# Ex 1
array_greater_than_3 = arr[arr > 3]
print(array_greater_than_3)

# Ex 2
squared_array = arr ** 2
print(squared_array)

# Ex 3
average_value = np.mean(arr)
array_greater_than_avg = arr[arr > average_value]
print(array_greater_than_avg)

# Ex 4
second_array = np.array([1, 2, 1, 2, 1, 2, 3])
elementwise_multiplication = arr * second_array
elementwise_division = arr / second_array
elementwise_addition = arr + second_array
print(elementwise_multiplication)
print(elementwise_division)
print(elementwise_addition)
