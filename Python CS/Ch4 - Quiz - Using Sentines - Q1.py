count = 0
number = input()

while number != 'stop':
    if int(number) < 0:
        count +=1
        
    number = input()
print(count)
