def simple_separator():
    return('*' * 10)

print(simple_separator() == '**********')  # True

def long_separator(count):
    return('*' * count)

print(long_separator(3) == '***')  # True
print(long_separator(4) == '****')  # True


def separator(simbol, count):
    return(simbol * count)

print(separator('-', 10) == '----------')  # True
print(separator('#', 5) == '#####')  # True


def hello_world():
    print(f'{"*" * 10} \n\n Hello World! \n\n{"#" * 10}')

hello_world()


def hello_who(who='World'):
    print(f'{"*" * 10} \n\n Hello {who}! \n\n{"#" * 10}')

hello_who()
hello_who('Max')
hello_who('Kate')

from functools import reduce
def pow_many(power, *args):
    itog = 0
    # for number in args:
    #     itog += number
    # return(itog ** power)
    return(reduce(lambda x, y: x + y, args) ** power)

print(pow_many(1, 1, 2) == 3)  # True -> (1 + 2)**1 == 3
print(pow_many(1, 2, 3) == 5)  # True -> (2 + 3)**1 == 5
print(pow_many(2, 1, 1) == 4)  # True -> (1 + 1)**2 == 4
print(pow_many(3, 2) == 8)  # True -> 2**3 == 8
print(pow_many(2, 1, 2, 3, 4) == 100)  # True -> (1 + 2 + 3 + 4)**2 == 10**2 == 100

def print_key_val(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} --> {value}')

print_key_val(name='Max', age=21)
print_key_val(animal='Cat', is_animal=True)

def my_filter(iterable, function):
    return(list(filter(function, iterable)))


print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3) == [4, 5])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2) == [2])  # True
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3) == [1, 2, 4, 5])  # True
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba') == ['a', 'b'])  # True