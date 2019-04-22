#  Read 10 numbers from user and find the average of all.
# a) Use comparison operator to check how many numbers are less than average and print them
# b) Check how many numbers are more than average.
# c) How many are equal to average.

number = map(int, input("please enter 10 numbers separated by space: ").split(" "))
number_list = list(number)
avg = sum(number_list) / len(number_list)
print("Average of numbers: " + str(avg))
less_than_avg = 0
more_than_avg = 0
equal_to_avg = 0
for n in number_list:
    if n < avg:
        less_than_avg += 1
    elif n > avg:
        more_than_avg += 1
    else:
        equal_to_avg += 1

print("No of items less than avg: " + str(less_than_avg))
print("No of items more than avg: " + str(more_than_avg))
print("No of items equal to avg: " + str(equal_to_avg))
