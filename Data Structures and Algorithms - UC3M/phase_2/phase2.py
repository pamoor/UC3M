"""
Case #2. Exercise  3
@author: EDA Team
"""

# Classes provided by EDA Team
from dlist import DList
from bintree import BinaryNode
from bst import BinarySearchTree
from avl import AVLTree
class BST2(BinarySearchTree):
    def find_dist_k(self, n: int, k:int) -> list:
         
        node = self.search(n)
        if not node:
            return []
        resultado = []
        if k == 0:
            resultado.append(node.elem)
        else:
            k -= self.depth(node)
            self._find_dist_k(self.root, k, True, resultado, n)
        return resultado


    def _find_dist_k(self,node: BinaryNode, k: int, camino: bool, resultado: list, n: int):
        
        if node is None:
            return
     
        if k == 0:
            resultado.append(node.elem)
        
        if node.elem == n:
            camino = False
            
        if camino:
            if node.elem > n:
                self._find_dist_k(node.left, k+1, True, resultado, n)
                if k > 0:
                    self._find_dist_k(node.right, k-1, False, resultado, n)
            else:
                if k > 0:
                    self._find_dist_k(node.left, k-1, False, resultado, n)
                self._find_dist_k(node.right, k+1, True, resultado, n)
        
        elif k > 0:
            self._find_dist_k(node.left, k-1, False, resultado, n)
            self._find_dist_k(node.right, k-1, False, resultado, n)
            

def create_tree(input_tree1: AVLTree, input_tree2: AVLTree, opc: str) -> AVLTree:
    
    resultado = AVLTree()
    
    
    if opc == "merge":
        if input_tree1 == input_tree2 or not input_tree2._root:
            return input_tree1
        
        elif not input_tree1._root:
            return input_tree2
        
        else:
            _mer(input_tree1._root, resultado)
            _mer(input_tree2._root, resultado)
            return resultado
    
    elif opc == "intersection":
        if input_tree1 == input_tree2:
            return input_tree1
        else:
            _int(input_tree1._root, input_tree2, resultado)
            return resultado
       
    elif opc == "difference":
        if input_tree1 == input_tree2:
            return resultado
        else:
            _diff(input_tree1._root, input_tree2, resultado)
            return resultado
    
    else:
        print("Operación no válida")
        return None
    
        

def _mer(node:BinaryNode, resultado: AVLTree):
    if not node:
        return
    else:
        if resultado.search(node.elem) is None:
            resultado.insert(node.elem)
        _mer(node.left, resultado)
        _mer(node.right,resultado)
        
def _int(node:BinaryNode, arbol2: AVLTree, resultado: AVLTree):
    if not node:
        return
    else:
        if arbol2.search(node.elem) is not None: 
            resultado.insert(node.elem)
        
        _int(node.left, arbol2, resultado)
        _int(node.right, arbol2, resultado)
           
def _diff(node:BinaryNode, arbol2: AVLTree, resultado: AVLTree):
    if not node:
        return
    else:
        if arbol2.search(node.elem) is None: 
            resultado.insert(node.elem)
        
        _diff(node.left, arbol2, resultado)
        _diff(node.right,arbol2,resultado)
 
            
    


# Some usage examples
if __name__ == '__main__':
    input_list = [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80,3,123,132,657,7654,234,132,34,34,6,7,54,2,5,]
    # input_list_01 = [5, 1, 7, 9, 23]
    # input_list_02 = [1, 9, 11]

    input_list_01 = [50, 55, 54]
    input_list_02 = [9, 3, 21]

    # Build and draw first tree
    tree1 = BinarySearchTree()
    for x in input_list_01:
        tree1.insert(x)
    tree1.draw()

    # Build and draw second tree
    tree2 = BinarySearchTree()
    for x in input_list_02:
        tree2.insert(x)
    tree2.draw()

    function_names = ["merge", "intersection", "difference"]

    for op_name in function_names:
        res = create_tree(tree1, tree2, op_name)
        print(f"-- resultado, n for {op_name} method. #{res.size()} nodes")
        res.draw()
