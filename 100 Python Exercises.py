########################################################################################################################
# find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# Using for loop
for i in range(2000, 3200):
    if not i % 7 and i % 5:
        print(i, end=',')
print('\n####################')
# Using generator and list Comprehension
my_list = [num for num in range(2000, 3000) if not num % 7 and num % 5]
print(my_list)

########################################################################################################################
# factorial of a given numbers
# Recursive Function


def factorial(num):
    fact = num
    if fact != 1:
        fact = fact * factorial(fact-1)
    return fact


print(factorial(8))

########################################################################################################################
#
