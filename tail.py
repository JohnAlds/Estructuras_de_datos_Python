from Node import Node_Tail

class Tail:

    def __init__(self):
        
        self.first = None
        self.last = None
        self.size = 0
    
    def queue(self, data):

        self.size += 1
        newNode = Node_Tail(data)

        if self.first is None:

            self.first = self.last = newNode
        else:

            self.last.setNext(newNode)
            self.last = newNode

    def dequeue(self):

        if self.first is None:

            print('Empty Tail')
            return None
        else:

            startNode = self.first.getData()

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

            print(current.getData())

            current = current.getNext()
            