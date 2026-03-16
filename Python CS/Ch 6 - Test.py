import random

# Get the number of random numbers you want to generate.
max_nums = int(input('How many numbers do you want? '))

# Write the numbers to a file.
number_file = open('numbers.txt', 'w')
for count in range(0, max_nums):
    number = random.randint(0, 100)
    number_file.write(f'{number}\n')
number_file.close()

# Open the file, read and display the numbers.
number_file = open('numbers.txt', 'r')

# Write code here that uses a loop to read
# each number from the file and prints it on
# the screen.
for count in range(0, max_nums):
    read_number = number_file.readline()
    print(count+1,' - ',read_number,end='')
number_file.close()
