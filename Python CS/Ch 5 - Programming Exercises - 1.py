# Exercise 1
#def main():
#    distKm = float(input("Enter distance in Kilometers:"))
#
#    distMiles = convert_to_miles(distKm)
#
#    print(distKm,'km is the same as',distMiles,'miles')
#
#def convert_to_miles(kilometers):
#    miles = kilometers*0.6214
#    return miles
#
#
#if __name__ == '__main__':
#    main()

#############################
#Exercise 2 - Skipped because it depends on exercise 6 from Chapter 2

#############################
# Exercise 3

#def main():
#    replacementCost = float(input('Enter the replacement cost:'))
#
#    minimumInsurance = find_minimum_insurance(replacementCost)
#    print(f'The minimum amount of insurance you should buy is ${minimumInsurance:,.0f}')
#
#def find_minimum_insurance(cost):
#    insurance = 0.8*cost
#    return insurance
#
#if __name__ == '__main__':
#    main()

#############################    
# Exercise 4

#def main():
#    loanPayment = float(input('Enter monthly loan payment:'))
#    insurance   = float(input('Enter monthly insurance:'))
#    gas         = float(input('Enter monthly gas:'))
#    oil         = float(input('Enter monthly oil:'))
#    tires       = float(input('Enter monthly tires:'))
#    maintenance = float(input('Enter monthly maintenance:'))
#
#    calculate_total_expenses(loanPayment,insurance,gas,oil,tires,maintenance)
#
#
#def calculate_total_expenses(loanPayment,insurance,gas,oil,tires,maintenance):
#    sum_monthly = loanPayment+insurance+gas+oil+tires+maintenance
#    sum_annual  = sum_monthly*12
#    print(f'The total monthly expenses are ${sum_monthly:,.0f} and the annual expenses are ${sum_annual:,.0f}')
#
#if __name__ == '__main__':
#    main()

#############################    
# Exercise 5 - Property Tax 

#def main():
#    propertyValue = float(input('Enter property value:'))
#
#    calculatePropertyTax(propertyValue)
#
#
#def calculatePropertyTax(propertyValue):
#    assessmentValue = propertyValue*0.6
#    propertyTax = (assessmentValue/100)*0.72
#    print(f'The assessment value for the property is ${assessmentValue:,.2f} and the property tax is ${propertyTax:,.2f}')
#
#if __name__ == '__main__':
#    main()
    
#############################    
# Exercise 6 - Stadium Seating

#def main():
#    seatsA = int(input("Enter number of Class A seats:"))
#    seatsB = int(input("Enter number of Class B seats:"))
#    seatsC = int(input("Enter number of Class C seats:"))

#    print(f'The income generated was ${incomeGenerated(seatsA,seatsB,seatsC):,.0f}')

#def incomeGenerated(seatsA,seatsB,seatsC):
#    priceA = 20
#    priceB = 15
#    priceC = 10
    

#    incomeGenerated = seatsA*priceA+seatsB*priceB+seatsC*priceC
#    return incomeGenerated
    

#if __name__ == '__main__':
#    main()

#############################    
# Exercise 7 - Paint Job Estimator

#def main():
#    wallArea    = float(input('Enter the square feet of wall to be painted:'))
#    gallonPrice = float(input('Enter the price of paint per gallon:'))

#    jobEstimator(wallArea,gallonPrice)

#def jobEstimator(wallArea,gallonPrice):
    #Parameters
#    sqFeetReference = 112
#    laborCostPerHour = 35
#    laborHoursPerSqFeet = 8/sqFeetReference
#    paintGallonperSqFeet = 1/sqFeetReference


#    paintGallonsRequired = paintGallonperSqFeet*wallArea
#    laborHoursRequired   = laborHoursPerSqFeet*wallArea
#    paintCost            = paintGallonsRequired*gallonPrice
#    laborCharges         = laborCostPerHour*laborHoursRequired
#    totalCost            = laborCharges+paintCost


#    print(f'This job will require {paintGallonsRequired:,.2f} gallons of paint and {laborHoursRequired:,.2f} hours of labor')
#    print(f'This job will cost ${totalCost:,.2f} in total with ${paintCost:,.2f} and ${laborCharges:,.2f} being paint cost and labor cost respectively')

#if __name__ == '__main__':
#    main()


#############################    
# Exercise 8 - Monthly Sales Tax


#############################    
# Exercise 10 - Math Quiz

#import random

#def main():

#    mathQuiz()

#def mathQuiz():
#    x1= random.randint(1,1000)
#    x2= random.randint(1,1000)
      
#    flagCorrect = 0
#    while flagCorrect == 0:
#        answer = float(input(f'What is {x1:,.0f} + {x2:,.0f}?'))
#        if answer == x1+x2:
#            print('Correct! Congratulations!')
#            flagCorrect = 1            
#        else:
#            print('Incorrect Try again!')
       
#if __name__ == '__main__':
#    main()


#############################    
# Exercise 14 - Test Average Grade


#############################    
# Exercise 15 - Odd/Even Counter


#############################    
# Exercise 16 - Prime Number Check

#############################    
# Exercise 17 - Iterate Exercise 16 to display all prime numbers from 1 to 100

#############################    
# Exercise 18 - Future Value

#############################    
# Exercise 19 - Random Number Guessing Game

#############################    
# Exercise 20 - Rock, Paper, Scissors Game
import random
import math

def main():
    flagWinner = 0
    while flagWinner == 0:
        numberComputerChoice = random.randint(1,3)
        
        if numberComputerChoice == 1:
            computerChoice = 'rock'
        elif numberComputerChoice == 2:
            computerChoice = 'paper'
        elif numberComputerChoice == 3:
            computerChoice = 'scissors'

        userChoice =input('Enter your choice among rock, paper, and scissors:')

        print(f'The Computer chose {computerChoice}')

        if computerChoice == userChoice:
            print('''It's a draw!Try again!''')
            userChoice =input('Enter your choice among rock, paper, and scissors:')
        if computerChoice == 'rock':
            if userChoice == 'paper':
                print('You won!')
                flagWinner = 1
            elif userChoice == 'scissors':
                print('You lost!')
                flagWinner = 1
                
        if computerChoice == 'paper':
            if userChoice == 'scissors':
                print('You won!')
                flagWinner = 1                
            elif userChoice == 'rock':
                print('You lost!')
                flagWinner = 1                

        if computerChoice == 'scissors':
            if userChoice == 'rock':
                print('You won!')
                flagWinner = 1                
            elif userChoice == 'paper':
                print('You lost!')
                flagWinner = 1                
        
    
if __name__ == '__main__':
    main()
          
    
