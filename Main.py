from inspect import stack
from doubleList_ import Double_List
from stack import Stack
from tail import Tail
from sparseMatrix import SparseMatrix

if __name__ == '__main__':

    
    '''stack_ = Stack()

    stack_.push(1)
    stack_.push(2)
    stack_.push(3)
    stack_.push(4)

    stack_.showStack()

    nodePop = stack_.pop()

    print('Al hacer pop: ' + str(nodePop.getDato()) + ' ahora la cima de la pila es: ' + str(stack_.top.getDato()))

    stack_.showStack()'''

    '''tail = Tail()

    tail.queue(1)
    tail.queue(2)
    tail.queue(3)
    tail.queue(4)
    tail.queue(5)

    tail.showTail()

    nodeD = tail.dequeue()

    print('Al desencolar: ' + str(nodeD.getDato()) + ', ahora el primero de la cola es: ' + str(tail.first.getDato()))

    tail.showTail()'''

    matriz = SparseMatrix()

    matriz.insert(1,1, 'Johnny')
    matriz.insert(1,2, 'Hasel')
    matriz.insert(1,3, 'Mafer')
    matriz.insert(2,1, 'Andrea')
    matriz.insert(2,2, 'Laura')
    matriz.insert(2,3, 'Ricardo')
    matriz.insert(3,1, 'Emily')
    matriz.insert(3,2, 'Jacky')
    matriz.insert(3,3, 'Diego')

    #matriz.tourRow(1)
    #matriz.tourColumn(1)

    matriz.show()


    

    


    
    
