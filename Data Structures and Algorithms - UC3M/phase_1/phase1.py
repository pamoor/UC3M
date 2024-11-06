from slistH import SList
from slistH import SNode

import sys

class SList2(SList):
    
    def __str__(self):
        result='['
        for n in range(self._size - 1):
           result += (str(self.getAt(n)) + ', ')
        result += (str(self.getAt(self._size - 1)) + ']')
        return result         
    
    def eq_slist_list(self, lista:list):
        
        if len(self) != len(lista):
            return False
        
        node_it = self._head
        n = 0
        
        while node_it:
            if node_it.elem != lista[n]:
                return False
            else:
                node_it = node_it.next
                n += 1
                
        return True

    
    def del_largest_seq(self) -> None: 
        """Este método identifica la última secuencia más larga de números idénticos y consecutivos en la lista y la elimina"""
    
        if self.isEmpty():
            return
        
        else:
            longitud_mayor = 1
            longitud_it = 1
            cota_mayor = 0
            indice_it = 0
            node_it = self._head
            node2 = node_it.next
        
            while node2:

                if node_it.elem == node2.elem:
                    longitud_it +=1
                    
                    if longitud_it >= longitud_mayor:
                        longitud_mayor = longitud_it
                        cota_mayor = indice_it + 1
    
                else:
                    longitud_it = 1
                    
                node_it = node2
                node2 = node2.next
                indice_it += 1
            
            if longitud_mayor == 1:
                self.removeLast()
                
            else: 
                node1 = self._head
                node2 = self._head
                
                #Localizamos el nodo previo a la racha a eliminar
                for _ in range(cota_mayor - longitud_mayor):
                    node1 = node1.next
                
                #Localizamos el último nodo de la racha    
                for _ in range(cota_mayor):
                    node2 = node2.next
                
                #Apuntamos el nodo de antes de la racha al siguiente de la misma y actualizamos el tamaño    
                node1.next = node2.next
                self._size -= longitud_mayor
                
                


                
                
    def fix_loop(self)->bool:
        """detecta un bucle, y en caso afirmativo devuelve un True y quita el bucle, en caso contrario devuelve False"""

        # complejidad O(n)
        if self.isEmpty():
           return False

        else:
            #Inicializamos dos nodos al head
            node1 = self._head
            node2 = node1
            #damos el primer paso en node1(slow)
            node1 = node1.next
            
            if node1 is None:
                return False
            #si el siguiente del head es None, la lista es de longitud 1
            
            else:
                node2 = node1.next
            
            while node2 and node1 != node2:
                node1 = node1.next
                node2 = node2.next
                if node2:
                    node2 = node2.next

            if not node2:
                return False
            
            else:
                node1 = self._head
                
                
                if node1 == node2:
                    # CUANDO EL BUCLE OCUPA TODA LA LISTA
                    while node2.next != node1:
                        node2 = node2.next
                
                else:
                    #CUANDO EL BUCLE NO SE DA EN EL PRIMER NODO
                    while node2.next != node1.next:
                        node1 = node1.next
                        node2 = node2.next
                                  
                node2.next = None
                return True
            
            
    def create_loop(self, position):
        # this method is used to force a loop in a singly linked list
        if position < 0 or position > len(self) - 1:
            raise ValueError(f"Position out of range [{0} - {len(self) - 1}]")

        current = self._head
        i = 0

        # We reach position to save the reference
        while current and i < position:
            current = current.next
            i += 1

        # We reach to tail node and set the loop
        start_node = current
        print(f"Creating a loop starting from {start_node.elem}")
        while current.next:
            current = current.next        
        current.next = start_node
		
		
    def left_right_shift(self,left,n):
        if self.isEmpty() or n <= 0 or n >= len(self):
            return   
        else:
                
            if left is True:
                node_it = self._head
                contador = 1
                #voy al nodo n-ésimo
                while contador < n:
                    node_it = node_it.next
                    contador +=1
                #nodo_apoyo se queda fijo en el n-ésimo
                nodo_apoyo = node_it
                #voy al último nodo
                while node_it.next:
                    node_it = node_it.next
                
                #apunto el next del último nodo al actual head
                node_it.next = self._head
                #cambio el head al next del n-ésimo
                self._head = nodo_apoyo.next
                #el n-ésimo se convierte en el tail, por eso apunta a None
                nodo_apoyo.next = None

            elif left is False:
                node_it = self._head
            
                #El pseudohead será el tail:
                while node_it.next:
                    node_it = node_it.next
                else:
                    #modifico n para señalar hasta qué nodo tiene que ir(irá hasta el prev al que hay que empezar a cambiar)
                    n = len(self) - n
                    
                    nodo_apoyo = self._head
                    contador = 1
                    
                    while contador<n and nodo_apoyo:
                        nodo_apoyo = nodo_apoyo.next
                        contador +=1
                    #nodo_apoyo es el nodo n-ésimo
                    #Apunto el next del tail al head
                    node_it.next = self._head
                    #convierto el head en el next del n-ésimo
                    self._head = nodo_apoyo.next
                    #el n-ésimo se convierte en el tail, por eso apunta a None
                    nodo_apoyo.next = None
                    
                    
                    
                
            
if __name__=='__main__':
    l=SList2()
    for i in [10,20,30,40,50,60,70]:
         l.addLast(i)

    print("Lista original:",l)
    l.left_right_shift(True, 2)
    print("Lista después de left = True:", l)
    
    l2 = SList2()
    for i in [10,20,30,40,50,60,70]:
         l2.addLast(i)
    
    print("Lista original:",l2)
    l2.left_right_shift(False, 2)
    print("Lista después de left = False:", l2)
    
    l3 = SList2()
    l3.addLast(2)
    l3_2 = SList2()
    l3_2.addFirst(2)
    l3.left_right_shift(False,1)
    print(l3)
    
    print(l3 == l3_2)
    
    