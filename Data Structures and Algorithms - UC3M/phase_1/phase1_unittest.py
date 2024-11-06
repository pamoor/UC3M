

import unittest
from phase1 import SList2

class Test(unittest.TestCase):
    
    # -----TESTS EJERCICIO 1-----
    
    def test_1_1(self):
        """Si la lista introducida está vacía devolverá un mensaje de error y continuará vacía"""
        lista = SList2()
        lista.del_largest_seq()
        self.assertTrue(lista.isEmpty())
        
    def test_1_2(self):
        """Si la lista tiene un solo elemento  devolverá una lista vacía"""
        lista = SList2()
        lista.addLast(1)
        lista.del_largest_seq()
        self.assertTrue(lista.isEmpty())
        
    def test_1_3(self):
        """La lista eliminará la secuencia de mayor número de elementos consecutivos iguales"""
        lista = SList2()
        esperada = [3,33,4,5,6,6,6,2]
        for elem in [3,33,4,5,6,6,6,7,7,7,7,2]:
            lista.addLast(elem)
        lista.del_largest_seq()
        print("Lista obtenida:", str(lista))
        print("Lista esperada:", str(esperada))
        self.assertTrue(lista.eq_slist_list(esperada))
        
    def test_1_4(self):
        """La lista eliminará  en concreto  la última secuencia de mayor número de elementos consecutivos iguales"""
        lista = SList2()
        esperada = [3,33,4,5,6,6,6,6,2]
        for elem in [3,33,4,5,6,6,6,6,7,7,7,7,2]:
            lista.addLast(elem)
        lista.del_largest_seq()
        print("Lista obtenida:", str(lista))
        print("Lista esperada:", str(esperada))
        self.assertTrue(lista.eq_slist_list(esperada))
        
    def test_1_5(self):
        """A igualdad de longitudes  la función eliminará únicamente la última"""
        lista = SList2()
        esperada = [2,2,3,3,5,5,8,8]
        for elem in [2,2,3,3,5,5,8,8,12,12]:
            lista.addLast(elem)
        lista.del_largest_seq()
        print("Lista obtenida:", str(lista))
        print("Lista esperada:", str(esperada))
        self.assertTrue(lista.eq_slist_list(esperada))
        
    def test_1_6(self):
        """La función eliminará el último elemento en el caso de que no haya ninguno igual (secuencia 1)"""
        lista = SList2()
        esperada = [1,2,3,4,5]
        for elem in [1,2,3,4,5,6]:
            lista.addLast(elem)
        lista.del_largest_seq()
        print("lista obtenida:", str(lista))
        self.assertTrue(lista.eq_slist_list(esperada))
        
        
    #--------------------------------------------------------------------------------------------------------

    #----------------------------------TESTS EJERCICIO 2-----------------------------------------------------
        
        
    def test2_1(self):
            """La lista será vacía"""
            lista = SList2()
            self.assertFalse(lista.fix_loop())

    def test2_2(self):
        """La lista será de longitud 1"""
        lista = SList2()
        lista.addLast(1)
        self.assertFalse(lista.fix_loop())
        
    def test2_3(self):
        """La lista no tendrá bucles"""
        lista = SList2()
        for elem in [2,3,5,6,6,7,2,3,7,6]:
            lista.addLast(elem)
        self.assertFalse(lista.fix_loop())

    def test2_4(self):
        """La lista tendrá longitud 1 y encerrará un bucle"""
        lista = SList2()
        lista.addLast(1)
        lista.create_loop(0)
        self.assertTrue(lista.fix_loop())
        node_it = lista._head
        self.assertIsNone(node_it.next)

    
    #TESTS DE LISTAS PARES
    def test2_5(self):
        """La lista tendrá longitud par y encerrará un bucle en el último nodo"""
        lista = SList2()
        
        for elem in [16,3,5,6,6,12,2,3,9,6]:
            lista.addLast(elem)
            
        lista.create_loop(9)
        
        
        node_it = lista._head
        
        for _ in range(lista._size - 1):
            node_it = node_it.next
        
        self.assertTrue(lista.fix_loop())    
        
        expected = node_it.next        
        
        self.assertIsNone(expected)
        
    def test2_6(self):
        """La lista tendrá longitud par y encerrará un bucle entre la mitad y el final"""
        lista = SList2()
        
        for elem in [16,3,5,6,6,12,2,3,9,6]:
            lista.addLast(elem)
            
        lista.create_loop(6)
        
        
        node_it = lista._head
        
        for _ in range(lista._size - 1):
            node_it = node_it.next
        
        self.assertTrue(lista.fix_loop())    
        
        expected = node_it.next        
        
        self.assertIsNone(expected)
    
    def test2_7(self):
        """La lista tendrá longitud par y encerrará un bucle en el nodo del medio"""
        lista = SList2()
        
        for elem in [16,3,5,6,6,12,2,3,9,6]:
            lista.addLast(elem)
            
        lista.create_loop(4)
        
        
        node_it = lista._head
        
        for _ in range(lista._size - 1):
            node_it = node_it.next
        
        self.assertTrue(lista.fix_loop())    
        
        expected = node_it.next        
        
        self.assertIsNone(expected)
    
    def test2_8(self):
        """La lista tendrá longitud par y encerrará un bucle entre el primer nodo y el de la mitad"""
        lista = SList2()
        
        for elem in [16,3,5,6,6,12,2,3,9,6]:
            lista.addLast(elem)
            
        lista.create_loop(2)
        
        
        node_it = lista._head
        
        for _ in range(lista._size - 1):
            node_it = node_it.next
        
        self.assertTrue(lista.fix_loop())    
        
        expected = node_it.next        
        
        self.assertIsNone(expected)
        
        
        
    def test2_9(self):
        """La lista tendrá longitud par y encerrará un bucle al principio"""
        lista = SList2()
        
        for elem in [16,3,5,6,6,12,2,3,9,6]:
            lista.addLast(elem)
            
        lista.create_loop(0)
        
        node_it = lista._head
        
        for _ in range(lista._size - 1):
            node_it = node_it.next
        
        self.assertTrue(lista.fix_loop())    
        
        expected = node_it.next        
        
        self.assertIsNone(expected)
                
    
        
    def test2_12(self):
        """La lista tendrá longitud par y todos los elementos iguales"""
        lista = SList2()
        
        for elem in [1,1,1,1,1,1]:
            lista.addLast(elem)
            
        lista.create_loop(0)
        
        node_it = lista._head
        
        for _ in range(lista._size - 1):
            node_it = node_it.next
        
        self.assertTrue(lista.fix_loop())    
        
        expected = node_it.next        
        
        self.assertIsNone(expected)
                
        
    
    #TEST DE LISTAS IMPARES
    
    def test2_10(self):
        """La lista tendrá longitud impar y encerrará un bucle en el último nodo"""
        lista = SList2()
        
        for elem in [1,5,7,8,9,7,8,5,6]:
            lista.addLast(elem)
            
        lista.create_loop(8)
        
        
        node_it = lista._head
        
        for _ in range(lista._size - 1):
            node_it = node_it.next
        
        self.assertTrue(lista.fix_loop())    
        
        expected = node_it.next        
        
        self.assertIsNone(expected)
    
    def test2_11(self):
        """La lista tendrá longitud impar y encerrará un bucle entre la mitad y el último nodo"""
        lista = SList2()
        
        for elem in [1,5,7,8,9,7,8,5,6]:
            lista.addLast(elem)
            
        lista.create_loop(6)
        
        
        node_it = lista._head
        
        for _ in range(lista._size - 1):
            node_it = node_it.next
        
        self.assertTrue(lista.fix_loop())    
        
        expected = node_it.next        
        
        self.assertIsNone(expected)
        
    def test2_12(self):
        """La lista tendrá longitud impar y encerrará un bucle entre la mitad y el primer nodo"""
        lista = SList2()
        
        for elem in [1,5,7,8,9,7,8,5,6]:
            lista.addLast(elem)
            
        lista.create_loop(3)
        
        
        node_it = lista._head
        
        for _ in range(lista._size - 1):
            node_it = node_it.next
        
        self.assertTrue(lista.fix_loop())    
        
        expected = node_it.next        
        
        self.assertIsNone(expected)
        
    
    def test2_11(self):
        """La lista tendrá longitud impar y encerrará un bucle en el primer nodo"""
        lista = SList2()
        
        for elem in [1,5,7,8,9,7,8,5,6]:
            lista.addLast(elem)
            
        lista.create_loop(0)
        
        
        node_it = lista._head
        
        for _ in range(lista._size - 1):
            node_it = node_it.next
        
        self.assertTrue(lista.fix_loop())    
        
        expected = node_it.next        
        
        self.assertIsNone(expected)
        
    
    def test2_13(self):
        """La lista tendrá longitud par y todos los elementos iguales"""
        lista = SList2()
        
        for elem in [1,1,1,1,1,1,1]:
            lista.addLast(elem)
            
        lista.create_loop(0)
        
        node_it = lista._head
        
        for _ in range(lista._size - 1):
            node_it = node_it.next
        
        self.assertTrue(lista.fix_loop())    
        
        expected = node_it.next        
        
        self.assertIsNone(expected)
                
    
#--------------------------------------------------------------------------------------------------------

#----------------------------------TESTS EJERCICIO 3-----------------------------------------------------

    def test3_1(self):
        """Aplicando el método a una lista vacía"""
        lista = SList2()
        lista.left_right_shift(True, 1)
        self.assertTrue(lista.isEmpty())
        
    def test3_2(self):
        """Método aplicado a una lista con longitud 1"""
        lista = SList2()
        lista.addFirst(2)
        lista.left_right_shift(True, 1)
        self.assertTrue(lista.eq_slist_list([2]))
        
    def test3_3(self):
        """Método aplicado a una lista con una longitud menor que n"""
        lista = SList2()
        lista.addFirst(2)
        lista.addFirst(3)
        lista.left_right_shift(True, 3)
        self.assertTrue(lista.eq_slist_list([3,2]))
        
    def test3_4(self):
        """Método en el que se introduce una n igual o inferior a 0"""
        lista = SList2()
        lista.addFirst(2)
        lista.addFirst(3)
        lista.left_right_shift(True, 0)
        self.assertTrue(lista.eq_slist_list([3,2]))
        
# Aplicación del método con distintos valores de n y de left

    def test3_5(self):
        lista = SList2()
        esperada = [3,4,5,6,7,1,2]
        for n in [1,2,3,4,5,6,7]:
            lista.addLast(n)
        lista.left_right_shift(True, 2)
        print("Lista obtenida:", str(lista))
        print("Lista esperada:", str(esperada))
        self.assertTrue(lista.eq_slist_list(esperada))
        
    def test3_6(self):
        lista = SList2()
        esperada = [2,3,4,5,6,7,1]
        for n in [1,2,3,4,5,6,7]:
            lista.addLast(n)
        lista.left_right_shift(True, 1)
        print("Lista obtenida:", str(lista))
        print("Lista esperada:", str(esperada))
        self.assertTrue(lista.eq_slist_list(esperada))
        
    def test3_7(self):
        lista = SList2()
        esperada = [5,6,7,1,2,3,4]
        for n in [1,2,3,4,5,6,7]:
            lista.addLast(n)
        lista.left_right_shift(True, 4)
        print("Lista obtenida:", str(lista))
        print("Lista esperada:", str(esperada))
        self.assertTrue(lista.eq_slist_list(esperada))
        
    def test3_8(self):
        lista = SList2()
        esperada = [6,7,1,2,3,4,5]
        for n in [1,2,3,4,5,6,7]:
            lista.addLast(n)
        lista.left_right_shift(False, 2)
        print("Lista obtenida:", str(lista))
        print("Lista esperada:", str(esperada))
        self.assertTrue(lista.eq_slist_list(esperada))
        
    def test3_9(self):
        lista = SList2()
        esperada = [7,1,2,3,4,5,6]
        for n in [1,2,3,4,5,6,7]:
            lista.addLast(n)
        lista.left_right_shift(False, 1)
        print("Lista obtenida:", str(lista))
        print("Lista esperada:", str(esperada))
        self.assertTrue(lista.eq_slist_list(esperada))
        
    def test3_10(self):
        lista = SList2()
        esperada = [4,5,6,7,1,2,3]
        for n in [1,2,3,4,5,6,7]:
            lista.addLast(n)
        lista.left_right_shift(False, 4)
        print("Lista obtenida:", str(lista))
        print("Lista esperada:", str(esperada))
        self.assertTrue(lista.eq_slist_list(esperada))
        
#--------------------------------------------------------------------------------------------------------
           
# Ejecutamos todos los test       
if __name__ == "__main__":
    unittest.main()