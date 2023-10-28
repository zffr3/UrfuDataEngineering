import csv

with open('text_4_var_77', encoding='utf-8') as File:
    reader = csv.reader(File) 
    resFile = open("result.txt", "a+", encoding='utf-8')
    resStr = ''
    filteredData = []
    averageIncome = 0
    averageCounter = 0
    ageFilter = 25 + 7
    for i in reader:
        filteredData.append((int(i[0]),i[1],i[2],i[3],i[4]))
        averageIncome += int(i[4][:-1])
        averageCounter +=1
    averageIncome = int(averageIncome / averageCounter)
    filteredData.sort()
    for i in filteredData:
        if (int(i[4][:-1]) > averageIncome) & (int(i[3]) > ageFilter):
            resStr = resStr + str(i[0]) + ' ' + i[1] + ' ' + i[2] + ' ' + i[3] + ' ' + i[4] + '\n'
    resFile.write(resStr)
    resFile.close()