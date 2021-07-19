# Command pattern
#
# You can keep track of commands, such that you can do and
# undo. Using plain methods that would be hard to implement,
# but with the command pattern you keep track of the history

import os

class MoveFileCommand(object):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst 
        os.rename(self.src, self.dst)

    def undo(self):
        os.rename(self.dst, self.src)

stack = []
stack.append(MoveFileCommand('hello.txt','foo.txt'))
stack.append(MoveFileCommand('foo.txt','bar.txt'))

stack.pop().undo()
stack.pop().undo()
