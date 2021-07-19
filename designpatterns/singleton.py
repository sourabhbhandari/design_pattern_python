# Singleton pattern
#
# There can be one and only one object of the given class
#

class Car:
    _instance = None

    def getInstance():
        if Car._instance == None:
            Car()
        return Car._instance
    
    def __init__(self):
        if Car._instance != None:
            raise Exception("Singleton: there can only be one object")
        else:
            Car._instance = self

obj = Car()
print(obj)

obj2 = Car.getInstance()
print(obj2)


