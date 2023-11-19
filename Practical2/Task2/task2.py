import numpy as np
import os

matrix = np.load('matrix_77_2.npy')
x_result = []
y_result = []
z_result = []
x = 0
y = 0

for i in matrix:
    for j in i:
        if j > 577:
            x_result.append(x)
            y_result.append(y)
            z_result.append(j)
        y+=1
    x += 1
    
np.savez('result.npz', x_result, y_result, z_result)
np.savez_compressed('result_compressed.npz', x_result, y_result, z_result)

print(f"размер npz в байтах: {os.path.getsize('result.npz')}")
print(f"размер сжатого npz в байтах: {os.path.getsize('result_compressed.npz')}")