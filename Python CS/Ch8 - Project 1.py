password = input()
adjusted_ch=''
adjusted_ch_ord=0
key = 3

for ch in password:
    adjusted_ch_ord = ord(ch) +key

    adjusted_ch = adjusted_ch+chr(adjusted_ch_ord)

print(adjusted_ch)
