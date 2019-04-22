# Using loop structures print numbers from 1 to 100.
# and using the same loop print numbers from 100 to 1 (reverse printing)
# a) By using For loop
print("#" * 100)
for i in range(1, 101):
    print(i, end=" ")
print('\n')
for i in range(100, 0, -1):
    print(i, end=" ")
print("#" * 100)
# b) By using while loop
i = 1
while i <= 100:
    print(i, end=" ")
    i += 1
print('\n')
i = 100
while i > 0:
    print(i, end=' ')
    i -= 1
# c) Let mystring ="Hello world"
# print each character of mystring in to separate line using appropriate loop structure.
print("#" * 100)
mystring = "Hello world"

for char in mystring:
    print(char, end=" ")
