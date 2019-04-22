# Write a program to read string and print each character separately.

name = str(input('please enter your name:  '))
print('printing each characters of your name:')
for char in name:
    print(char)
# a) Slice the string using slice operator [:] slice the portion the strings to create a sub strings.

print('printing part of your name:')
substring = name[2:]
print(substring)

# b) Repeat the string 100 times using repeat operator *
print('printing name 100 times: {}'.format(name * 100))

# c)Read string 2 and concatenate with other string using + operator.

s1 = str(input('enter 1st string:  '))
s2 = str(input('enter 2nd string: '))

print(s1 + s2)
