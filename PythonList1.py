# Write a program to create two list A & B such that List A contains Employee Id,
#  List B contain Employee name (minimum 10 entries in each list) & perform following operation

A = [12, 67, 70, 80, 90, 23, 45, 11, 19, 33]
B = ['Kapil', 'Kamal', 'Vimala', 'Shankar', 'Amit', 'Adi', 'Kishore', 'Teja', 'Tridib', 'Ravi']

# a) Print all names on to screen
for name in B:
    print(name)
# b) Read the index from the  user and print the corresponding name from both list.
index = int(input("please choose the index between 1-9: "))
if 0 < index <= 10:
    print('Employee details for {} index is {} {}'.format(index, A[index - 1], B[index - 1]))
else:
    index = int(input("please choose the index between 1-9: "))
# c) Print the names from 4th position to 9th position
print(A[3:9])
# d) Print all names from 3rd position till end of the list
print(A[2:])
# e) Repeat list elements by specified number of times (N- times, where N is entered by user)
print(A * 4)
# f) Concatenate two lists and print the output.
print(A + B)
# g) Print element of list A and B side by side.(i.e. List-A First element, List-B First element )
C = []
for i, n in enumerate(A):
    C.append(A[i])
    C.append(B[i])

print(C)
