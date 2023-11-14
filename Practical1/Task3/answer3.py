f = open('text_3_var_77', 'r')
result = open('result.txt', 'a+')
filterPoint = 50 + 77
content = f.readlines()
for i in content:
    nums = i.split(',')
    row = ''
    for (index,item) in enumerate(nums):
        if (item == 'NA') | (item == '\n'):
            nums[index] = int((int(nums[index-1]) + int(nums[index+1]))/2)
        if int(int(nums[index]) ** 0.5) > filterPoint:
            row += str(nums[index]) + ' ' 
    result.write(row + '\n')

result.close()
f.close()
