########################################
#
# CSC 157-8C1 Python Computer Science I
# Dept. of CS - OAKTON COLLEGE
# 
# Summer 2025 - MIDTERM
# Chapter 5: Programming  Exercise 17. Prime Number List
# 
# Date: 07/03/2025   <=========
#
# Author: FERNANDO CHIAVERINI ALBANO PEREIRA <======== IMPORTANT
#
########################################

# Must use the following starter code
# main function
def main():
    # local variable
    totalNumbers = 100
    print('number', '\t', 'is prime')
    print('------------------------')

    # For each number,
    # IF number is prime: print (number, '\t', 'prime')
    # ELSE: print (number, '\t', 'not prime')

    for number in range(1,totalNumbers+1):
        is_prime_flag = is_prime(number)
        if is_prime_flag == True:
                print (number, '\t', 'prime')
        else:
                print (number, '\t', 'not prime')
                
# define the is_prime function
# it receives a number as a parameter,
# and returns True if number is prime, False otherwise. 
def is_prime(number):
    # This function assumes 1 is NOT prime by pulling from the definition below.
    # Prime number definition: A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers. 
    # Source: https://en.wikipedia.org/wiki/Prime_number

   count_Divisors = 0
   divisor = 1
   while divisor <= number:
     if number%divisor == 0:
         count_Divisors += 1
     divisor += 1
   
   if count_Divisors == 2:
        return True
   else:
        return False
    
# Call the main function.
main()

