from  Node import Node

class Double_List:

    def __init__(self):
        
        self.first = None
        self.last = None
        self.size = 0

    #insert node at end
    def insert(self, dato):

        self.size += 1
        nuevo = Node(dato)

        if self.first == None:

            self.first = self.last = nuevo
        else:

            nuevo.setPrevious(self.last)
            self.last.setNext(nuevo)
            self.last = nuevo

    #insert node at start
    def insertStart(self, dato):

        self.size += 1
        nuevo = Node(dato)

        if self.first == None:

            self.first = self.last = nuevo
        else:

            self.first.setPrevious(nuevo)
            nuevo.setPrevious(self.first)
            self.first = nuevo

    #show elements
    def showElements(self):

        current = self.first

        while  current != None:

            print(current.getDato())

            current = current.getNext()

    #insert in alphabetical order
    def insertAlphabetical(self, dato):

        nuevo = Node(dato)
        self.size += 1
        
        if self.first == None:

            self.first = self.last = nuevo
        
        else:

            current = self.first

            while current != None:

                if nuevo.getDato() < current.getDato():

                    if current == self.first:

                        nuevo.setNext(self.first)
                        self.first.setPrevious(nuevo)
                        self.first = nuevo
                        break
                    else:
                        
                        nuevo.setNext(current)
                        nuevo.setPrevious(current.getPrevious())
                        current.getPrevious().setNext(nuevo)
                        current.setPrevious(nuevo)
                        
                        break
                
                elif nuevo.getDato() > current.getDato():

                    if current == self.last:

                        nuevo.setPrevious(current)
                        current.setNext(nuevo)
                        self.last = nuevo
                        break
                    else:

                        current = current.getNext()

                elif nuevo.getDato() == current.getDato():

                    current = current.getNext()
    
    #insert Before
    def insertBefore(self, insertDato, beforeDato):

        if self.first is None:

            print('Lista vacía.')
        else:

            current  =  self.first

            while current is not None:

                if current.getDato() == beforeDato:

                    break

                current = current.getNext()

            if current is None:

                print(beforeDato + ' no se encuentra en la lista.')
            else:

                nuevo = Node(insertDato)
                nuevo.setNext(current)
                nuevo.setPrevious(current.getPrevious())

                if current.getPrevious() is not None:

                    current.getPrevious().setNext(nuevo)
                else:
    
                    self.first = nuevo
                
                current.setPrevious(nuevo)
        
    #insert later
    def insertLater(self, insertDato, laterDato):

        if self.first is None:

            print('Lista vacía')

        else:

            current = self.first

            while current is not None:

                if current.getDato() == laterDato:

                    break

                current = current.getNext()
            
            if current is None:

                print( laterDato + ' no se encuentra en la lista.')
            else:

                nuevo = Node(insertDato)
                nuevo.setPrevious(current)
                nuevo.setNext(current.getNext())

                if current.getNext() is not None:

                    current.getNext().setPrevious(nuevo)
                
                current.setNext(nuevo)

    #pop
    def pop(self):

        if self.first == None:

            print('Lista vacía, no hay nada que sacar')
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



