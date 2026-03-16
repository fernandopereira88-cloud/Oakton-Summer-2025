fixed_capital=''
flag_caps = 0
fixed=''
sentence=input()

for index in range(len(sentence)):
    #print(sentence[index],'Caps',flag_caps)
    if sentence[index] == '.':
        fixed = fixed +sentence[index].upper()
        flag_caps = 1
    elif flag_caps == 1 and sentence[index] != ' ':
        fixed = fixed +sentence[index].upper()
        flag_caps=0

    elif index == 0:
        fixed = fixed +sentence[index].upper()
    else:
        fixed = fixed + sentence[index].lower()
print(fixed)


