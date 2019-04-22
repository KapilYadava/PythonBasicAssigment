# Create a tuple with at least 10 elements having integer values in it;
# Print all elements
# Perform slicing operations
# Perform repetition with * operator
# Perform concatenation with other tuple.


li = (12, 34, 56, 67, 89, 45, 56, 33, 55, 22, 22, 19)
li2 = (1, 2, 4, 5)

print('printing all elements available in the tuple: ')
for item in li:
    print(item, end=" ")

print('\nperforming slicing operation in tuple')
print(li[:5])
print(li[5:])
print(li[3:8])

print('Performing repetition with * operator')
print(li * 2)

print('performing concatenation with other tuple')
print(li + li2)
print(li2 + li)
print(li)
