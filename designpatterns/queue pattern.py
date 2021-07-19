# Queue pattern
#
# Queues are a collection of objects. Python implements the
# queue pattern using the module queue.

import queue

class Car:
    def __init__(self, name):
        self.name = name
    
    def showName(self):
        print(self.name)


obj1 = Car("volvo")
obj2 = Car("bmw")
obj3 = Car("crysler")
obj4 = Car("opel")

q = queue.LifoQueue()
q.put(obj1)
q.put(obj2)
q.put(obj3)
q.put(obj4)

while not q.empty():
    obj = q.get()
    obj.showName()
