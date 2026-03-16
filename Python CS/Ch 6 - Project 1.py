
myfile = open('numbers.txt','r')
sum_pos = 0
count_pos = 0
sum_neg = 0
count_neg = 0
avg_neg = 0
avg_pos = 0

for line in myfile:
        number = float(line.rstrip('\n'))

        if number > 0:            
            sum_pos = sum_pos +number
            count_pos = count_pos +1
            
        elif number < 0:            
            sum_neg = sum_neg +number
            count_neg = count_neg +1

avg_neg = sum_neg/(count_neg+1)
avg_pos = sum_pos/count_pos


if count_neg == 0 and count_pos == 0:
        print('NaN')
else:        
        print(avg_neg)
        print(avg_pos)

myfile.close()
