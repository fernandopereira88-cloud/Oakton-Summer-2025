#Ask for colors
color1 = input("Enter the first color:")
color2 = input("Enter the second color:")

#Validate input
if (color1 !='red' and  color1 !='green' and  color1 !='yellow' and  color1 !='purple' and  color1 !='blue' and  color1 !='orange') or (color2 !='red' and  color2 !='green' and  color2 !='yellow' and  color2 !='purple' and  color2 !='blue' and  color2 !='orange'):
    print("You did not enter one of red, orange, yellow, green, blue or purple")

#Check for complementary colors
elif (
        (color1 == 'red' and color2 == 'green')
    or (color1 == 'green' and color2 == 'red')
    or (color1 == 'yellow' and color2 == 'purple')
    or (color1 == 'purple' and color2 == 'yellow')
        or (color1 == 'blue' and color2 == 'orange')
        or (color1 == 'orange' and color2 == 'blue')
    ):
        
    print("The two colors are complementary")
else:
    print("The two colors are not complementary")
