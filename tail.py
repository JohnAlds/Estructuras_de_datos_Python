

from Node import Node


class Tail:

    def __init__(self):
        
        self.first = None
        self.last = None
        self.size = 0
    
    def queue(self, data):

        self.size += 1
        nuevo = Node(data)

        if self.first is None:

            self.first = self.last = nuevo
        else:

            nuevo.setPrevious(self.last)
            self.last.setNext(nuevo)
            self.last = nuevo

    def dequeue(self):

        if self.first is None:

            print('Lista vacía.')
        else:

            startNode = Node(self.first.getDato())

            if self.first is self.last:

                self.first = self.last = None
                self.size -= 1

                return startNode
            else:

                self.first = self.first.getNext()
                self.size -= 1

                return startNode
    
    def showTail(self):

        current = self.first

        while current is not None:

            print(current.getDato())

            current = current.getNext()
            