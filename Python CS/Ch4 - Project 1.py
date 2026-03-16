#prompts the user to enter a number within the range of 1 through 100.
number=float(input('Enter a number from 1 throught 100:'))

#When the user enters a valid number,
#the program should display a multiplication table showing the user's number
#multiplied by the values 1 through 10.
while number < 1 or number > 100:
    number=float(input('Enter a number from 1 throught 100:'))

for n in range(1,11):
    product = number*n
    print(f'{number:,.0f} x {n} = {product:,.0f}')
