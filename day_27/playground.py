def add(*args):
    # prints the argument in position 1
    print(args[1])

    sum = 0
    for n in args:
        sum += n
    print(sum)


add(1, 2, 6)


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #   print(key)
    #   print(value)
    n += kwargs["add"]
    n += kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Vauxhall", model="Corsa")

print(my_car.seats)
