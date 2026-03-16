# Initialize the denominator to its first value in the list. 
denominator = 30
total = 0 
# Write a for statement for the numerator with start/end limits. 
for numerator in range (1,31):
    value = numerator / denominator
    total = total + value 
    # Decrement the denominator. 
    denominator = denominator - 1
print (total)
