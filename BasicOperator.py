# Write a program to find the biggest of 3 numbers (Use If Condition)

a, b, c = map(int, input('Enter three numbers separated by common:  ').split(','))


def get_biggest_number(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3


# Write a program to find given number is odd or Even

def is_even(n1):
    if n1 % 2 == 0:
        return True
    return False


# Write a program to find the number is Prime or not.


def is_prime(n1):
    for n in range(2, n1 - 1):
        if n1 % n == 0:
            return False
    return True


print('Biggest Number is {}'.format(get_biggest_number(a, b, c)))

if is_even(a):
    print("Number {} is even".format(a))
else:
    print("Number {} is odd".format(a))

if is_prime(a):
    print("Number {} is prime".format(a))
else:
    print("Number {} is not prime".format(a))
