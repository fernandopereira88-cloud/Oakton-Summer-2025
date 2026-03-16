
number = int(input("Enter a positive integer: "))

    
if number > 0 and number % 2 == 0 and number % 3 == 0 and number % 5 == 0 :
    print("The number is magic.")
elif number <=  0:    
    print("You can only input positive integers.")
else:
    print("The number is not magic.")
