# Create a list of 5 names and check given name exist in the List.

names = ['Kapil', 'Azzad', 'Amit', 'Shankar', 'Alka']
# a) Use membership operator (IN) to check the presence of an element.
name = 'Alka'
if name in names:
    print('name is already available in the list')
else:
    print('name is not available in the list')

# b) Perform above task without using membership operator.

print(names.__contains__("Kapil"))

# c) Print the elements of the list in reverse direction.

for n in reversed(names):
    print(n)
