from re import U
from Node import Node_Stack

class Stack:

    def __init__(self):

        self.first : Node_Stack = None
        self.top : Node_Stack = None
        self.size = 0

    def push(self, data):

        self.size += 1
        newNode = Node_Stack(data)

        if self.first is None: 

            self.first = self.top = newNode
        else:

            self.top.setUp(newNode)
            self.top = newNode

    def pop(self):
    
        if self.first == None:

            print('Empty stack.')
        else:

            dataTop = self.top.getData()

            if self.first == self.top:

                self.first = self.top = None
                self.size -= 1

                return dataTop
            else:

                current = self.first
                self.size -= 1

                while current.getUp() != self.top:

                    current = current.getUp()
                
                self.top = current
                self.top.setUp(None)

                return dataTop

    def showStack(self):

        top = self.first

        while top is not None:

            print(top.getData())

            top = top.getUp()

