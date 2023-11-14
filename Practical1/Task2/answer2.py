f = open('text_2_var_77', 'r')
resFileSum = open('resultSum.txt', 'a+')
resFileAv = open('resultAver.txt', 'a+')

lines = f.read().split('\n')
for i in lines:
    nums = i.split('|')
    summ = 0
    aveSumm = 0
    aveCount = 0
    if i != '':
        for j in nums:
            if j != '':
                if int(j) % 2 == 0:
                    summ += int(j)
                else:
                    aveSumm += int(j)
                    aveCount +=1
        resFileSum.write(str(summ) + '\n')
        resFileAv.write(str(aveSumm/aveCount) +'\n')

resFileSum.close()
resFileAv.close()
f.close()
