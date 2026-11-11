import numpy as np


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

print(hours[2])
print(hours[-1])
print(hours[2:6])
print(hours[::2])
print(hours[::-1])

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