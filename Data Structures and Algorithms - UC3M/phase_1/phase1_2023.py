from slistH import SList
from slistH import SNode


class SList2(SList):
    
    def del_largest_seq(self) -> None: 
        if self._head is None:
            return None

        if len(self) == 1:
            self._head = None
            return None

        # At least, two elements
        # Keep pointers to (start-1), end and length of the largest sequence
        largest_prev_to_start = self._head
        largest_pointer_to_end = self._head
        largest_length = 1
        # Keep pointer to (start-1) and length of the current sequence
        current_prev_to_start = self._head
        current_length = 1

        it_prev = self._head  # pointer to the previous element respect to it
        it = self._head.next  # iterator through the list

        while it:
            if it.elem == it_prev.elem:
                # Keep the seq. One more element in the seq
                current_length += 1
            else:
                # A new seq. starts...
                # Comparing to equal to include the sequence most at the right as the one to delete
                if current_length >= largest_length:
                    # And the last one is the largest
                    largest_prev_to_start = current_prev_to_start
                    largest_pointer_to_end = it_prev
                    largest_length = current_length
                # Reset length and pointer to start of the new sequence
                current_prev_to_start = it_prev
                current_length = 1
            it_prev = it
            it = it.next

        # It is None but maybe the last sequence is the largest
        if current_length >= largest_length:
            largest_prev_to_start = current_prev_to_start
            largest_pointer_to_end = it_prev
            largest_length = current_length

        # remove the largest seq, checking if the largest one starts at _head, and it is at beginning of the list
        if largest_prev_to_start == self._head and self._head.elem == largest_pointer_to_end.elem:
            # The largest one is at the beginning. Set _head accordingly
            self._head = largest_pointer_to_end.next
        else:
            # Not at the beginning. Remove all elements in one step
            largest_prev_to_start.next = largest_pointer_to_end.next
        self._size -= largest_length
        

    def __break_loop(self, node: SNode) -> None:
        """
        This solution is based on https://www.geeksforgeeks.org/detect-and-remove-loop-in-a-linked-list/
        node is a pointer to a node within the loop
        O(n)
        """
        # As node is within the loop, I can count how many nodes are within the loop
        ptr1 = node
        ptr2 = node

        # Count the number of nodes in loop
        k = 1
        while ptr1.next != ptr2:
            ptr1 = ptr1.next
            k += 1

        # Fix one pointer to head.
        # And the other pointer to k nodes after head
        ptr1 = self._head
        ptr2 = self._head
        for _ in range(k):
            ptr2 = ptr2.next

        # Move both pointers at the same rate/place
        # they will meet at loop starting node
        while ptr2 != ptr1:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        # Get pointer to the last node
        while ptr2.next != ptr1:
            ptr2 = ptr2.next

        # Set the next node of the loop ending node
        # to fix the loop
        ptr2.next = None

    def fix_loop(self) -> bool:
        """
        This solution is based on Floyd's cycle finding algorithm
        https://www.geeksforgeeks.org/floyds-cycle-finding-algorithm/
        """
        # Two pointers at the beginning
        slow_pointer = self._head
        fast_pointer = self._head

        found = False

        # Check not None for the two pointers and one more in the fast pointer
        while slow_pointer and fast_pointer and fast_pointer.next:
            # Increment pointers: slow by one, fast by two
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                # Cycle found! Flag and fix it
                # Both slow and fast point to a node within the loop
                self.__break_loop(slow_pointer)
                found = True
        return found

    def create_loop(self, position):
        # this method is used to force a loop in a singly linked list
        # It is part of the solution, not coded by me
        if position < 0 or position > len(self) - 1:
            raise ValueError(f"Position out of range [{0} - {len(self) - 1}]")

        current = self._head
        pos = 0

        # We reach position to save the reference
        while current and pos < position:
            current = current.next
            pos += 1

        # We reach to tail node and set the loop
        start_node = current
        print(f"Creating a loop starting from {start_node.elem}")
        while current.next:
            current = current.next        
        current.next = start_node

    def left_right_shift(self, left: bool, n: int) -> None:
        # According to reqs, do nothing if n is >= size of the list
        # This validation also includes if list is zero/1 element long
        if n == 0 or n >= self._size:
            print("n == 0 or n >= self._size")
            return

        # Find the k-node position where the list is going to be split
        if left:
            # n nodes starting from the left. Position starts at 0
            k = n - 1
        else:
            # n nodes starting from the right. Position starts at 0
            k = self._size - n - 1

        # Move to the k-node
        node_to_splitting_point = self._head
        for _ in range(k):
            node_to_splitting_point = node_to_splitting_point.next

        # And a pointer to the end
        node_tail = node_to_splitting_point.next
        while node_tail.next:
            node_tail = node_tail.next

        # And finally adjust pointers to link elements in the proper way
        node_tail.next = self._head
        self._head = node_to_splitting_point.next
        node_to_splitting_point.next = None



