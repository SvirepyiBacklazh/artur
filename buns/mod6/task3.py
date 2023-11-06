def is_armstrong_number(number):
    number_str = str(number)
    power = len(number_str)
    sum_of_powers = sum(int(digit) ** power for digit in number_str)
    return number == sum_of_powers

def armstrong_number_generator():
    number = 10
    while True:
        if is_armstrong_number(number):
            yield number
        number += 1

generator = armstrong_number_generator()

def get_next_armstrong_number():
    return next(generator)

for _ in range(8):
    print(get_next_armstrong_number(), end='')
