# Prototype pattern
#
# Sometimes creating a new object is computationally expensive.
# In that case, you can clone the object and modify it.


from copy import deepcopy
import time

class Prototype(object):
    def clone(self):
        return deepcopy(self)

class NetworkConnector(Prototype):
    def __init__(self):
        self.name = "expensive method here"
        time.sleep(5)
        print("object created")

obj = NetworkConnector()
print(obj.name)

obj2 = obj.clone()
print(obj2.name)
