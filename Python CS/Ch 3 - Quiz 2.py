password = 'a'
counter = 0
while password != 'python123':
    password = input("Enter the password:")    
    if password != 'python123':
        counter +=1
print('Number of invalid attempts:',counter)
