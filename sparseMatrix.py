from tracemalloc import start
from Node import Head_Node, Internal_Node
from headList import Head_List

class SparseMatrix:

    def __init__(self):
        
        self.numberRows = 0
        self.numberColumn = 0
        self.rows = Head_List('row')
        self.column = Head_List('column')

    def insert(self, posX, posY, data):

        newCeld = Internal_Node(posX, posY, data)

        nodeX = self.rows.getHead(posX)
        nodeY = self.column.getHead(posY)

        if nodeX is None:

            self.numberRows += 1
            nodeX = Head_Node(posX)
            self.rows.insert_headNode(nodeX)
        
        if nodeY is None:
    
            self.numberColumn += 1
            nodeY = Head_Node(posY)
            self.column.insert_headNode(nodeY)

        #------------------------------------------
        if nodeX.getAccess() == None:

            nodeX.setAccess(newCeld)
        else:

            if newCeld.getY() < nodeX.getAccess().getY():

                newCeld.setRight(nodeX.getAccess())
                nodeX.getAccess().setLeft(newCeld)
                nodeX.setAccess(newCeld)
            else:

                temp : Internal_Node = nodeX.getAccess()

                while temp is not None:

                    if newCeld.getY() < temp.getY():

                        newCeld.setRight(temp)
                        newCeld.setLeft(temp.getLeft())
                        temp.getLeft().setRight(newCeld)
                        temp.setLeft(newCeld)
                        break
                    elif newCeld.getX() == temp.getX() and newCeld.getY() == temp.getY():

                        break
                    else:

                        if temp.getRight() == None:
                            temp.setRight(newCeld)
                            newCeld.setLeft(temp)
                            break;
                        else:
                            temp = temp.getRight() 
        #---------------------------------------

        if nodeY.getAccess() == None:
    
            nodeY.setAccess(newCeld)
        else:

            if newCeld.getX() < nodeY.getAccess().getX():

                newCeld.setDown(nodeX.getAccess())
                nodeY.getAccess().setUp(newCeld)
                nodeY.setAccess(newCeld)
            else:

                temp2 : Internal_Node = nodeY.getAccess()

                while temp2 is not None:

                    if newCeld.getX() < temp2.getX():

                        newCeld.setDown(temp2)
                        newCeld.setUp(temp2.getUp())
                        temp2.getUp().setDown(newCeld)
                        temp2.setUp(newCeld)
                        break
                    elif newCeld.getX() == temp2.getX() and newCeld.getY() == temp2.getY():

                        break
                    else:

                        if temp2.getDown() == None:
                            temp2.setDown(newCeld)
                            newCeld.setUp(temp2)
                            break;
                        else:
                            temp2 = temp2.getDown() 

    def tourRow(self, row):

        start = self.rows.getHead(row)

        if start == None:
            
            print('Esa coordenada de filas no existe')
            
            
        temp : Internal_Node = start.getAccess()
        
        while temp != None:
            print(temp.getX(), temp.getY(), temp.getData())  
            temp = temp.getRight()

    def tourColumn(self, column):
    
        start = self.column.getHead(column)

        if start == None:
            
            print('Esa coordenada de columnas no existe')
            
            
        temp : Internal_Node = start.getAccess()
        
        while temp != None:
            print(temp.getData())  
            temp = temp.getDown()

    def show(self):
        
        start = self.rows.first.getId()
        last = self.rows.last.getId()
        
        i = start
        
        for j  in range(start, last + 1):
            
            self.tourRow(i)
            
            i +=  1