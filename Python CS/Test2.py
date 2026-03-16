new_file = open('words.txt','w')

new_file.write('rain\n')
new_file.write('sunshine\n')
new_file.write('sunshine\n')
new_file.write('sunshine\n')
new_file.write('rain\n')
new_file.write('sunshine\n')
new_file.write('sunshine\n')
new_file.write('sunshine\n')
new_file.write('rain\n')
new_file.write('sunshine\n')
new_file.write('sunshine\n')
new_file.write('sunshine\n')
new_file.close()


new_file = open('words.txt','r')

for line in new_file:
    print(line)
