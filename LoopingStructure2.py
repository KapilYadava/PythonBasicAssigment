# Using loop structures print even numbers between 1 to 100.
# a) By using For loop, use continue/ break/ pass statement to skip odd numbers.

for i in range(1, 100):
    if i % 2 == 0:
        print(i, end=" ")
        continue
print("#" * 100)
# i) Break the loop if the value is 50
for i in range(1, 100):
    if i == 50:
        break
    print(i, end=" ")

# ii) Use continue for the values 10,20,30,40,50
print("#" * 100)
for i in range(1, 100):
    if i == 10 or i == 20 or i == 30 or i == 40 or i == 50:
        continue
    print(i, end=" ")

# b) By using while loop, use continue/ break/ pass statement to skip odd numbers.
# i) Break the loop if the value is 90

print("#" * 100)
i = 1
while i < 100:
    i += 1
    if i % 2 == 0:
        print(i, end=' ')
        continue

# ii) Use continue for the values 60,70,80,90

print("#" * 100)
i = 1
while i < 100:
    i += 1
    if i == 60 or i == 70 or i == 80 or i == 90:
        continue
    print(i, end=' ')
