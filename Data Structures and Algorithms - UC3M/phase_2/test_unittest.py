# -*- coding: utf-8 -*-
"""
Test program comparing solutions with the builtin list-based one.

@author: EDA Team
"""

# Classes provided by EDA Team
from bst import BinarySearchTree
from phase2 import BST2
from avl import AVLTree
from phase2 import create_tree
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.Arbol = BST2()
        
        for x in [14,11,18,10,13,16,19,5,12,15,17,30,4,6,29,31,2,8,24,33,1,3,7,9,23,25,32,34,21,27,36,20,22,26,28,35,37]:
            self.Arbol.insert(x)
        self.Arbol.draw()

   
    # Estos test provienen de los ejemplos del pdf con las instrucciones de la fase 2
    
    def test_test01(self):
        self.assertEqual(self.Arbol.find_dist_k(30, 0), [30])
        
    def test_test02(self):
        self.assertEqual(self.Arbol.find_dist_k(30, 2), [18,24,33])
        
    def test_test03(self):
        self.assertEqual(self.Arbol.find_dist_k(12,6), [2,8,15,17,30])
        
    def test_test04(self):
        self.assertEqual(self.Arbol.find_dist_k(17, 7), [4,6,23,25,32,34])
        
    def test_test05(self):
        self.assertEqual(self.Arbol.find_dist_k(26,9), [11,15,17,36])
    
    # Arbol vacío
    def test_test06(self):
        Arbolvacio = BST2()
        self.assertEqual(Arbolvacio.find_dist_k(26,9), [])
    
    # Nodo que no esta en el árbol    
    def test_test06(self):
        Arbolvacio = BST2()
        self.assertEqual(Arbolvacio.find_dist_k(38,9), [])
        

    
    def testcreate_tree_merge01(self):
        #Merge con todos los elementos distintos
    
        arbol1 = AVLTree()
        arbol2=AVLTree()
        input_list_01 = [50, 55, 54]
        input_list_02 = [9, 3, 21]
        resultado = AVLTree()

        for x in input_list_02:
            arbol2.insert(x)
   
        for x in input_list_01:
            arbol1.insert(x)
        
        
        prueba = BST2()
        prueba = create_tree(arbol1,arbol2,"merge")
        for x in [50,55,54,9,3,21]:
            resultado.insert(x)

        self.assertEqual(prueba.size(),6)
        self.assertEqual(prueba,resultado)
    
    
    def testcreate_tree_merge02(self):
        #Merge con elementos duplicados 
        arbol1 = AVLTree()
        arbol2=AVLTree()
        input_list_01 = [50, 55, 54]
        input_list_02 = [9, 55, 54,44,67]
        resultado = AVLTree()

        for x in input_list_02:
            arbol2.insert(x)
   
        for x in input_list_01:
            arbol1.insert(x)
        
        
        prueba = BST2()
        prueba = create_tree(arbol1,arbol2,"merge")
        for x in [50,55,54,9,44,67]:
            resultado.insert(x)

        self.assertEqual(prueba.size(),6)
        self.assertEqual(prueba,resultado)
    
    def testcreate_tree_merge03(self):
        #Merge con dos árboles idénticos
        arbol1 = AVLTree()
        arbol2=AVLTree()
        input_list_01 = [50, 55, 54]
        input_list_02 = [50,55,54]
        resultado = AVLTree()

        for x in input_list_02:
            arbol2.insert(x)
   
        for x in input_list_01:
            arbol1.insert(x)
        
        
        prueba = AVLTree()
        prueba = create_tree(arbol1,arbol2,"merge")
        for x in [50,55,54]:
            resultado.insert(x)

        self.assertEqual(prueba.size(),3)
        self.assertEqual(prueba,resultado)
    
    def test_intersection01(self):
        #Árboles con nodos en común
       arbol1 = AVLTree()
       arbol2 = AVLTree()
       for x in [10,5,20]:
           arbol1.insert(x)
       for x in [20,5,25,30]:
           arbol2.insert(x)
       prueba = AVLTree()
       prueba = create_tree(arbol1,arbol2,"intersection")
       resultado = AVLTree()
       resultado.insert(5)
       resultado.insert(20)
       self.assertEqual(prueba, resultado)
    
    def test_intersection02(self):
        #Árboles sin nodos en común
       arbol1 = AVLTree()
       arbol2 = AVLTree()
     
       for x in [25,30]:
           arbol2.insert(x)
       prueba = create_tree(arbol1,arbol2,"intersection")
       resultado = AVLTree()
       
       

       self.assertEqual(prueba, resultado)
       
    
    def test_difference01(self):
        #Árboles sin nodos en común
        arbol1 = AVLTree()
        arbol2 = AVLTree()
        for x in [10,5,15]:
           arbol1.insert(x)
        for x in [20,25,30]:
           arbol2.insert(x)
        prueba = create_tree(arbol1, arbol2, "difference")
        resultado = arbol1
        self.assertEqual(prueba, resultado)  
    
    def test_difference02(self):
        #Árboles con nodos en común
        arbol1 = AVLTree()
        arbol2 = AVLTree()
        for x in [10,5,20]:
           arbol1.insert(x)
        for x in [20,25,30]:
           arbol2.insert(x)
        prueba = create_tree(arbol1, arbol2, "difference")
        resultado = AVLTree()
        for x in [10,5]:
            resultado.insert(x)
        self.assertEqual(prueba, resultado) 
        
    
    def test_operación_inválida (self):
        arbol1 = AVLTree()
        arbol2 = AVLTree()
        prueba = create_tree(arbol1,arbol2,"aaa")
        self.assertIsNone(prueba)


if __name__ == '__main__':
    unittest.main()
