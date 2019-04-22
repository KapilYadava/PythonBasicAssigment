# Write program to perform following:
# i) Check whether given number is prime or not.


def is_prime(n1):
    for n in range(2, n1 - 1):
        if n1 % n == 0:
            return False
    return True


num = 23
if is_prime(num):
    print("Number {} is prime".format(num))
else:
    print("Number {} is not prime".format(num))

# ii) Generate all the prime numbers between 1 to N where N is given number

for i in range(1, num):
    if is_prime(i):
        print(i)
