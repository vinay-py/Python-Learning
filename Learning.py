# List Comprehension
from time import time
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = [x for x in some_list if some_list.count(x) > 1]
print(duplicates)
duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
print(duplicates)
##############################################################################################################################################
# Decorators
# can be used for authenticating or logging or performance check or decorating a print line everytime a func runs
##############################################################################################################################################


def performance(fn):
    def wrapper(*args, **kwargs):
        T1 = time()
        result = fn(*args, **kwargs)
        T2 = time()
        print(f'took {T2-T1} seconds')
        return result
    return wrapper


@performance
def long_time():
    for i in range(1000000):
        i*5


long_time()

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': False
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
        else:
            print('User unauthorized to run the function')
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
##############################################################################################################################################
