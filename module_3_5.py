def get_multiplied_digits (numbers):
    str_number = str(numbers)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


a = get_multiplied_digits(40203)
print(a)
a = get_multiplied_digits(60403)
print(a)
a = get_multiplied_digits(82501)
print(a)