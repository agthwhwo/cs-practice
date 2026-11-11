import numpy as np

#task1
hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print("hours:", hours)
print("shape:", hours.shape)
print("ndim:", hours.ndim)
print("size:", hours.size)
print("dtype:", hours.dtype)

#task2
print(hours[2])
print(hours[-1])
print(hours[2:6])
print(hours[::2])
print(hours[::-1])

#task3
temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])
print(temperatures.shape)
print(temperatures.ndim)
print(temperatures.size)
print(temperatures[1, 2])
print(temperatures[0, :])
print(temperatures[:, -1])
print(temperatures[:2, 1:])
print(temperatures[:2, 1:3])

#task4
matrix = np.arange(1, 26).reshape(5, 5)
a1 = matrix[:3, :]
print(a1)
print(a1.shape)

a2 = matrix[-2:, :]
print(a2)
print(a2.shape)

a3 = matrix[:, :2]
print(a3)
print(a3.shape)

a4 = matrix[1:4, 2:5]
print(a4)
print(a4.shape)

a5 = matrix[-2:, -2:]
print(a5)
print(a5.shape)

#task5
vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0
print(vector)

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9
print(small_matrix)

#copy() нужна,чтобы изменения не изменяли исходный массив
changed_hours = hours.copy()

changed_hours[2:5] = 99
changed_hours[::2] = -1

print("changed_hours:", changed_hours)
print("hours:", hours)

changed_matrix = matrix.copy()

changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print("changed_matrix:")
print(changed_matrix)

print("matrix:")
print(matrix)
#task6
#reshape(3, 4) работает,потому что в исходном массиве 12 элементов(как мы задаём и в reshape 3 * 4 = 12) 
# а reshape(5, 3) вызовет ошибку,потому что 5 * 3 = 15,работа с массивом из 12 элементов не пройдёт
numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print("numbers:")
print(numbers)
print("shape:", numbers.shape)

print("table:")
print(table)
print("shape:", table.shape)

print("transposed:")
print(transposed)
print("shape:", transposed.shape)