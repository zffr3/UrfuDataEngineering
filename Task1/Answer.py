f = open('text_1_var_77', 'r')
fileContent = f.read()
characterFrequency = dict()
for i in fileContent:
    if characterFrequency.get(i,-1) == -1:
        characterFrequency[i] = 1
    else:
        characterFrequency[i] = characterFrequency[i] + 1
sortedFC = dict(sorted(characterFrequency.items()))

resFile = open("result.txt", "a+")

for key, value in characterFrequency.items():
    resFile.write(str(key) + ':' + str(value) + '\n')

resFile.close()
f.close()
