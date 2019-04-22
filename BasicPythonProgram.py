# Write a program to Add, Subtract, Multiply, and Divide 2 numbers


def add(c, d):
    return c + d


def sub(c, d):
    return c - d


def multiply(c, d):
    return c * d


def div(c, d):
    return c / d


a = int(input('Please enter a number  '))
b = int(input('Please enter another number  '))

print('Adding number {} and {} = {}'.format(a, b, add(a, b)))
print('Subtracting number {} and {} = {}'.format(a, b, sub(a, b)))
print('Multiplying number {} and {} = {}'.format(a, b, multiply(a, b)))
print('Dividing number {} and {} = {}'.format(a, b, div(a, b)))
