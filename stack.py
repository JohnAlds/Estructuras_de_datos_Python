from Node import Node

class Stack:

    def __init__(self):

        self.first : Node = None
        self.top : Node = None
        self.size = 0

    def push(self, data):

        self.size += 1

        if self.first is None:

            newNode = Node(data)
            self.first = self.top = newNode
        else:

            newNode = Node(data)
            
            self.top.setNext(newNode)
            newNode.setPrevious(self.top)
            self.top = newNode

    def pop(self):
    
        if self.first == None:

            print('Lista vacía, no hay nada que sacar')
        else:

            topNode = Node(self.top.getDato())

            if self.first == self.top:

                self.first = self.top = None
                self.size -= 1

                return topNode
            else:

                current = self.first
                self.size -= 1

                while current.getNext() != self.top:

                    current = current.getNext()
                
                self.top = current
                self.top.setNext(None)

                return topNode

    def showStack(self):

        top = self.top

        while top is not None:

            print(top.getDato())

            top = top.getPrevious()

