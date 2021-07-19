# Iterator pattern
#
# Iterator pattern lets you iterate over a collection of
# objects, numbers, strings etc.

class Car:
    pass

numbers = [Car(),Car(),Car(),Car()]

it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))


