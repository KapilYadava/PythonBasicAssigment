# Write a program to receive 5 command line arguments and print each argument separately.
# Example: >> python test.py arg1 arg2 arg3 arg4 arg5

# a) From the above statement your program should receive arguments and print them each of them.
arg = map(str, input('Please enter 5 input string separated by space:  ').split())

for item in arg:
    print(item)


# b) Find the biggest of three numbers, where three numbers are passed as command line arguments.


def get_biggest_number(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3


a, b, c = map(int, input('Please enter 3 numbers separated by space:  ').split())
print('Biggest Number is {}'.format(get_biggest_number(a, b, c)))
