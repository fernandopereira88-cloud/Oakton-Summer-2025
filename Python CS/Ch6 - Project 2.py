try:
    with open('fahrenheit.txt','r') as myfile, open('celsius.txt','w') as newfile:

        for line in myfile:
            number = float(line.rstrip('\n'))
            celsius = (number-32)*5/9
            newfile.write(f'{celsius:.2f}\n') 

except FileNotFoundError:
    print("File not found")

except ValueError:
    print("Invalid data")
    
