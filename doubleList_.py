from  Node import Node

class Double_List:

    def __init__(self):
        
        self.first = None
        self.last = None
        self.size = 0

    #insert node at end
    def insert(self, dato):

        self.size += 1
        newNode = Node(dato)

        if self.first == None:

            self.first = self.last = newNode
        else:

            newNode.setPrevious(self.last)
            self.last.setNext(newNode)
            self.last = newNode

    #insert node at start
    def insertStart(self, dato):

        self.size += 1
        newNode = Node(dato)

        if self.first == None:

            self.first = self.last = newNode
        else:

            self.first.setPrevious(newNode)
            newNode.setPrevious(self.first)
            self.first = newNode

    #show elements
    def showElements(self):

        current = self.first

        while  current != None:

            print(current.getDato())

            current = current.getNext()

    #insert in alphabetical order
    def insertAlphabetical(self, dato):

        newNode = Node(dato)
        self.size += 1
        
        if self.first == None:

            self.first = self.last = newNode
        
        else:

            current = self.first

            while current != None:

                if newNode.getDato() < current.getDato():

                    if current == self.first:

                        newNode.setNext(self.first)
                        self.first.setPrevious(newNode)
                        self.first = newNode
                        break
                    else:
                        
                        newNode.setNext(current)
                        newNode.setPrevious(current.getPrevious())
                        current.getPrevious().setNext(newNode)
                        current.setPrevious(newNode)
                        
                        break
                
                elif newNode.getDato() > current.getDato():

                    if current == self.last:

                        newNode.setPrevious(current)
                        current.setNext(newNode)
                        self.last = newNode
                        break
                    else:

                        current = current.getNext()

                elif newNode.getDato() == current.getDato():

                    current = current.getNext()
    
    #insert Before
    def insertBefore(self, insertDato, beforeDato):

        if self.first is None:

            print('Empty List.')
        else:

            current  =  self.first

            while current is not None:

                if current.getDato() == beforeDato:

                    break

                current = current.getNext()

            if current is None:

                print(str(beforeDato) + ' not found in the list.')
            else:

                newNode = Node(insertDato)
                newNode.setNext(current)
                newNode.setPrevious(current.getPrevious())

                if current.getPrevious() is not None:

                    current.getPrevious().setNext(newNode)
                else:
    
                    self.first = newNode
                
                current.setPrevious(newNode)
        
    #insert later
    def insertLater(self, insertDato, laterDato):

        if self.first is None:

            print('Empty List.')

        else:

            current = self.first

            while current is not None:

                if current.getDato() == laterDato:

                    break

                current = current.getNext()
            
            if current is None:

                print( str(laterDato) + ' not found in the list.')
            else:

                newNode = Node(insertDato)
                newNode.setPrevious(current)
                newNode.setNext(current.getNext())

                if current.getNext() is not None:

                    current.getNext().setPrevious(newNode)
                
                current.setNext(newNode)

    #pop
    def pop(self):

        if self.first == None:

            print('Empty List')
        else:

            top = Node(self.last.getDato())

            if self.first == self.last:

                self.first = self.last = None
                self.size -= 1

                return top
            else:

                current = self.first
                self.size -= 1

                while current.getNext() != self.last:

                    current = current.getNext()
                
                self.last = current
                self.last.setNext(None)

                return top



