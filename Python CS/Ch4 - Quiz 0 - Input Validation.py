# prompts the user for temperature
temperature = float(input("Enter the temperature:"))

# validates that temperature is within 78 to 100 (inclusive)
while temperature < 78 or temperature > 100:
    #If the user enters a value that is outside of this range, the program should prompt the user for the temperature again.
    temperature = float(input("Enter the temperature:"))
    #The program should continue prompting the user until they enter a value within the range.
#Once the user enters a valid temperature, the program should display "Temperature accepted."    
print('Temperature accepted.')
