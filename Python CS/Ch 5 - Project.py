
import math

def apothem(number_of_sides,side_length):
    return side_length / (2 * math.tan(math.radians(180 / number_of_sides)))

def area(number_of_sides,side_length):
    perimeter = number_of_sides * side_length
    
    return 0.5 * perimeter * apothem(number_of_sides,side_length)

def main():
    sides = int(input('Enter the number of sides:'))
    length = float(input('Enter the lenght of each side:'))

    print(f'{area(sides,length):.2f}')

main()

