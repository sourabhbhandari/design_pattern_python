# The factory pattern
#
# There is a factory method (make) which returns
# a new object, based on the function parameter
#

class CarFactory(object):
    def make(type):
        if type == "racecar":
            return RaceCar()
        elif type == "van":
            return Van()
        elif type == "bus":
            return Bus()

    make = staticmethod(make)
    

class Van:
    wheels = 4
    top_speed = 100

class Bus:
    wheels = 4
    top_speed = 80

class RaceCar:
    wheels = 4
    top_speed = 300

obj1 = CarFactory.make("bus")
obj2 = CarFactory.make("racecar")
obj3 = CarFactory.make("van")

print(obj1.top_speed)
print(obj2.top_speed)
