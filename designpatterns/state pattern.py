# state pattern
#
# Objects in real life can have multiple states
# This can be simulated in OOP using the state pattern
#

class ComputerState:
    name = "state"

    def switch(self, state):
        self.__class__ = state
        print(self.name)

    def __str__(self):
        return self.name

class On(ComputerState):
    name = "on"

class Off(ComputerState):
    name = "off"

class Hibernate(ComputerState):
    name = "hibernate"

class Suspend(ComputerState):
    name = "suspend"
    
class Computer:
    def __init__(self):
        print('Computer')
        self.state = Off()

    def change(self, state):
        self.state.switch(state)

obj = Computer()
obj.change(On)
obj.change(Off)
obj.change(Hibernate)
obj.change(Suspend)
obj.change(On)
obj.change(On)
