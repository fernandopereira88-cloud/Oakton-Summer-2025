########################################
#
# Final Exam:
# Type the code to solve this exam as specified
#
# CSC 157
# Dept. of CS - OAKTON COLLEGE
#
# Author: FERNANDO CHIAVERINI ALBANO PEREIRA
#
########################################

# Must use the following variables :
# total - for the sum of all the ints
# average - for the average of all the ints
number = 0
total = 0
count = 0
average = 0
number_list = []

# min - for the minimum of all the ints
# max - for the maximum of all the ints
firstTime = True
# min & max must be initalized in the loop

fileName = "numbers.txt"

# Open the numbers.txt file
inFile = open(fileName, mode="r")

# In the following for-loop read the ints in the numbers.txt file and
# compute  their total, average, min, and max 
for line in inFile:
    #
    # Find min, max, average, total in this loop
    # Remember: min & max must be initialized in the oop
    #
    number_list = line.split()
    
    for item in number_list:
        if firstTime == True:
            max = int(item)
            min = int(item)
            firstTime = False
            
        number = int(item)
        total += int(item)
        count += 1

        if number > max:
            max = number
        if number < min:
            min = number
            
    average = total/count

inFile.close()

# Display the: 
print("Total number of integers: ", count)
print("Total: ", total)
print("Average: ", average)
print("Minimum: ", min)
print("Maximum: ", max)

print("\nDone")


