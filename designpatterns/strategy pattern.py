# Strategy pattern
#
# Upon creation of a new object, define which implementation(s) # should be used. This can be algorithms or another method

import types 

class StrategyExample:
    def __init__(self, func = None):
        if func is not None:
            self.execute = types.MethodType(func, self)

    def execute(self):
        print(self.name)      

def execute_1(self):
    print('execute 1')

def execute_2(self):
    print('execute 2')

obj = StrategyExample(execute_1)
obj.execute()

obj2 = StrategyExample(execute_2)
obj2.execute()
