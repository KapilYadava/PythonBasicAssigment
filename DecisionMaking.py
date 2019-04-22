# Write a program to find the biggest of 4 numbers.
# a) Read 4 numbers from user using Input statement.
# b) extend the above program to find the biggest of 4 numbers.
# (PS: Use IF and IF & Else, If and ELIf, and Nested IF)


def biggest_number(n1, n2, n3, n4):
    if n1 > n2 and n1 > n3 and n1 > n4:
        return n1
    elif n2 > n1 and n2 > n3 and n2 > n4:
        return n2
    elif n3 > n1 and n3 > n2 and n3 > n4:
        return n3
    else:
        return n4


n1 = int(input('please enter first number: '))
n2 = int(input('please enter second number: '))
n3 = int(input('please enter third number: '))
n4 = int(input('please enter forth number: '))

print("Biggest number is {}".format(biggest_number(n1, n2, n3, n4)))
