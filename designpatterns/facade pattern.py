# Facade pattern
#
# This pattern abstracts various sub systems into one
# interface. You can see it as a wrapper pattern

class CPU:
    def execute(self):
        print('Run command')

class Memory:
    def load(self):
        print('Load in memory')

class Disk:
    def read(self):
        print('Read from disk')


class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.mem = Memory()
        self.disk = Disk()

    def start(self):
        self.cpu.execute()
        self.disk.read()
        self.mem.load()

    def stop(self):
        self.cpu.execute()


computer = ComputerFacade()
computer.start()
computer.stop()
