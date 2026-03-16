fh = open('fahrenheit.txt','w')
fh.write('abc\n')
fh.close()

try:
    myfile = open('fahrenheit.txt','r')
    newfile = open('celsius.txt','w')

    for line in myfile:
        number = float(line.rstrip('\n'))
        celsius = (number-32)*5/9
        newfile.write(f'{celsius:.2f}\n')
    newfile.close()
    myfile.close()

except FileNotFoundError:
    print("File not found")

except ValueError:
    print("Invalid data")
