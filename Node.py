
class Node:

    def __init__(self, dato):

        self.__dato = dato
        self.__next = None
        self.__previous = None

    #Getters
    def getDato(self):

        return self.__dato

    def getNext(self):

        return self.__next

    def getPrevious(self):

        return self.__previous

    #Setters
    def setDato(self, dato):

        self.__dato = dato
    
    def setNext(self, next):

        self.__next = next
    
    def setPrevious(self, previous):

        self.__previous = previous

class Head_Node:

    def __init__(self, id):
        self.__id = id
        self.__next = None
        self.__prev = None
        self.__access = None
    
    #Getters
    def getId(self):
    
        return self.__id

    def getNext(self):

        return self.__next

    def getPrev(self):

        return self.__prev

    def getAccess(self):

        return self.__access
    
    # Setters
    def setId(self, id):
    
        self.__id = id
    
    def setNext(self, next):

        self.__next = next
    
    def setPrevious(self, prev):

        self.__prev = prev

    def setAccess(self, access):

        self.__access = access
    
class Internal_Node:

    def __init__(self, x, y, data):
        
        self.__data = data
        self.__coord_X = x
        self.__coord_Y = y
        self.__up = None
        self.__down = None
        self.__left = None
        self.__right = None

    #Getters
    def getData(self):

        return self.__data

    def getX(self):
    
        return self.__coord_X
    
    def getY(self):
        
        return self.__coord_Y

    def getUp(self):

        return self.__up

    def getDown(self):

        return self.__down

    def getLeft(self):

        return self.__left

    def getRight(self):

        return self.__right

    #Setters
    def setData(self, data):
    
        self.__data = data

    def setX(self, x):
    
        self.__coord_X = x
    
    def setY(self, y):
        
        self.__coord_Y = y

    def setUp(self, up):

        self.__up = up

    def setDown(self, down):

        self.__down = down

    def setLeft(self, left):

        self.__left = left

    def setRight(self, right):

        self.__right = right

class Node_Tree:

    def __init__(self, data):
        
        self.__data = data
        self.__left = None
        self.__right = None

    # Getters
    def getData(self):
        return self.__data
    
    def getLeft(self):
        return self.__left
    
    def getRight(self):
        return self.__right

    #Setters
    def setData(self, data):
        self.__data = data
    
    def setLeft(self, left):
        self.__left = left
    
    def setRight(self, right):
        self.__right = right

class Node_Stack:

    def __init__(self, data):

        self.__data = data
        self.__up = None
    
    #Getters
    def getData(self):

        return self.__data
    
    def getUp(self):

        return self.__up

    #Setters
    def setData(self, data):

        self.__data = data
    
    def setUp(self, up):

        self.__up = up

class Node_Tail:

    def __init__(self, data):

        self.__data = data
        self.__next = None
    
    #Getters
    def getData(self):

        return self.__data
    
    def getNext(self):

        return self.__next

    #Setters
    def setData(self, data):

        self.__data = data
    
    def setNext(self, next):

        self.__next = next

