from Node import Node_Tree
import os
import webbrowser

class BSTree:

    def __init__(self):
        
        self.root = None
        self.graphviz = ''

    # Insert data
    def insert(self, data):
        
        if self.root == None:

            newNode = Node_Tree(data)
            self.root = newNode
        else:   

            self._insert(self.root, data)
    
    def _insert(self, node: Node_Tree, data):

        if data < node.getData():

            if node.getLeft() == None:

                newNode = Node_Tree(data)
                node.setLeft(newNode)
            else:

                self._insert(node.getLeft(), data)
        
        elif data > node.getData():

            if node.getRight() == None:

                newNode = Node_Tree(data)
                node.setRight(newNode)
            else:

                self._insert(node.getRight(), data)

    #Tours
    #Inorden
    def inorden(self):

        if self.root is None:

            print(' Empty BSTree.')
        else:

            self._inorden(self.root)
    
    def _inorden(self, node: Node_Tree):

        if node != None:

            self._inorden( node.getLeft())
            print(str(node.getData()) + ' ')
            self._inorden( node.getRight())
    
    #Preorden
    def preorden(self):

        if self.root is None:

            print(' Empty BSTree.')
        else:

            self._preorden(self.root)

    def _preorden(self, node: Node_Tree):

        if node != None:

            print(str(node.getData()) + ' ')
            self._preorden( node.getLeft())
            self._preorden( node.getRight())

    #Postorden
    def postorden(self):

        if self.root is None:

            print(' Empty BSTree.')
        else:

            self._postorden(self.root)

    def _postorden(self, node: Node_Tree):

        if node != None:

            self._postorden( node.getLeft())
            self._postorden( node.getRight())
            print(str(node.getData()) + ' ')
    
    #Graphviz
    def graph(self):

        self.graphviz = ''
        self.graphviz = 'digraph BST{\nnode[shape= box, fillcolor="#FFFFFF", style= filled];\nbgcolor = "#00FF7F";\nranksep = 0.5;\nnodesep = 0.5;\nsubgraph cluster_A{\nlabel = "Arbol Binario de Busqueda";\nbgcolor = "#20B2AA";\nfontcolor = white;\nfontsize = 30;\n\n '

        self.preordenGraph()

        self.graphviz += '}\n}';

        with open('grafico.txt', 'w') as file:

            file.write(self.graphviz)

        os.system('dot.exe -Tpdf grafico.txt -o grafico.pdf')
        webbrowser.open('grafico.pdf')
    

    def preordenGraph(self):

        if self.root is None:

            print('Empty BSTree.')
        else:

            self._preordenGraph(self.root)
    
    def _preordenGraph(self, node: Node_Tree):

        if node is not None:

            if node.getLeft() != None:

                self.graphviz += str(node.getData()) + ' -> ' + str(node.getLeft().getData()) + '\n'
            if node.getRight() != None:

                self.graphviz += str(node.getData()) + ' -> ' + str(node.getRight().getData()) + '\n'
            
            self._preordenGraph(node.getLeft())
            self._preordenGraph(node.getRight())
