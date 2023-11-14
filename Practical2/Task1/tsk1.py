import numpy as np
import json

matrix = np.load('matrix_77.npy')

summ = np.sum(matrix)
avr = np.mean(matrix)
maxx = matrix.max()
minn = matrix.min()

sumMd = 0
avrMd = 0
mainDiag = np.diag(matrix)

sumSd = 0
avrSd = 0
secondDiag = np.diag(np.fliplr(matrix))

frobeniusNorm = np.linalg.norm(matrix, 'fro')
normalizedMatrix = matrix / frobeniusNorm

for i in mainDiag:
    sumMd += i
    avrMd += 1
avrMd = sumMd / avrMd

for i in secondDiag:
    sumSd += i
    avrSd += 1   
avrSd = sumSd / avrSd

resultJs = {
    'sum': int(summ),
    'avr': int(avr),
    'sumMD': int(sumMd),
    'avrMD': int(avrMd),
    'sumSD': int(sumSd),
    'avrSD': int(avrSd),
    'max': int(maxx),
    'min': int(minn) 
}

with open('result.json', 'w') as jresult:
    json.dump(resultJs, jresult)

np.save('normalized_matrix_77', normalizedMatrix)