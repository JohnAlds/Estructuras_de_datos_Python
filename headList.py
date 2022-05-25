from Node import Head_Node

class Head_List:

    def __init__(self, type):

        self.type = type
        self.first = None
        self.last = None
        self.size = 0

    def insert_headNode(self, newNode : Head_Node): 

        if self.first is None:

            self.first = self.last = newNode
            self.size += 1
        else:

            if newNode.getId() < self.first.getId():
                
                newNode.setNext(self.first)
                self.first.setPrevious(newNode)
                self.first = newNode
                self.size += 1
            
            elif newNode.getId() > self.last.getId():

                self.last.setNext(newNode)
                newNode.setPrevious(self.last)
                self.last = newNode
                self.size += 1
            
            else:

                temp = self.first

                while temp !=  None:

                    if newNode.getId() < temp.getId():

                        newNode.setNext(temp)
                        newNode.setPrevious(temp.getPrev())
                        temp.getPrev().setNext(newNode)
                        temp.setPrevious(newNode)
                        self.size += 1

                        break
                    elif newNode.getId() > temp.getId():

                        temp = temp.getNext()
                    else:

                        break

    def show_listHead(self):
        
        current = self.first
        
        while current != None:
            
            print('fila: ' + str(current.getId()))
            current = current.getNext()

    def getHead(self, id):
        
        current = self.first
        
        while current != None:
            
            if id == current.getId():
                
                return current
            
            current = current.getNext()
        
        return None
