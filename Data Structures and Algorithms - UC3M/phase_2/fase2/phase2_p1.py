"""
Case #2. Exercise  1. The last version
@author: EDA Team
"""

# Classes provided by EDA Team
from bintree import BinaryNode
from bst import BinarySearchTree


"""
    Auxiliar functions to navigate through the tree hierarchy
"""


def get_parent(root: BinaryNode, node: BinaryNode) -> BinaryNode:
    # Find the parent of a given node in a tree, being root argument its root
    # If not found, return None
    if root is None or node is None or root.elem == node.elem:
        return None

    # A possible parent matches its left child elem with the node elem
    if root.left is not None and root.left.elem == node.elem:
        return root

    # Idem but with respect to right child elem
    if root.right is not None and root.right.elem == node.elem:
        return root

    # No matches! Keep searching, using BST is an ordered tree
    if node.elem < root.elem:
        return get_parent(root.left, node)
    else:
        return get_parent(root.right, node)


"""
    BST2 is a new class that includes the solution of exercise #1.
    find_dist_k
"""


class BST2(BinarySearchTree):
    def __rec_down_find_dist_k(self, node: BinaryNode, k: int, the_list: list) -> None:
        if node is not None:
            if k == 0:
                the_list.append(node.elem)
            else:
                self.__rec_down_find_dist_k(node.left, k-1, the_list)
                self.__rec_down_find_dist_k(node.right, k-1, the_list)

    def __rec_up_find_dist_k(self, node: BinaryNode, k: int, the_list: list) -> None:
        node_parent = get_parent(self.root, node)
        if node is not None and node_parent is not None:
            # If we reach root (node is not None AND node_parent is None), that is a base case
            # In the previous step of recursive calls, we had already processed descendants of
            # root in the other branch, if any.
            if k == 0:
                the_list.append(node_parent.elem)
            else:
                # Process nodes down in the tree
                # Only to search in the part that has not been already processed
                # At least, one part exists. So, searching is in the other part if exists
                # 1. Coming from the left part of the (sub)tree -> continue with the right part
                if node_parent.left is not None and node_parent.left.elem == node.elem:
                    if node_parent.right is not None:
                        self.__rec_down_find_dist_k(node_parent.right, k-1, the_list)

                # 2. Coming from the right part of the (sub)tree -> continue with the left part
                if node_parent.right is not None and node_parent.right.elem == node.elem:
                    if node_parent.left is not None:
                        self.__rec_down_find_dist_k(node_parent.left, k-1, the_list)

                # Process nodes up in the tree
                self.__rec_up_find_dist_k(node_parent, k-1, the_list)

    def find_dist_k(self, n: int, k: int) -> list:
        # Returns list of nodes, that starting at n are at k nodes of distance
        # n and k are positive int
        # If n is not in the tree, an empty list is returned
        n_node = self.search(n)

        # Process nodes down in the tree
        list_result = []
        self.__rec_down_find_dist_k(n_node, k, list_result)

        # Process nodes up in the tree
        if k > 0:
            self.__rec_up_find_dist_k(n_node, k-1, list_result)

        # list_result.sort()

        return list_result


# Test cases coming from the Isa's solution
if __name__ == '__main__':
    input_tree = BST2()
    for x in [50, 25, 30, 60, 20, 5, 31, 23, 65, 22, 28]:
        input_tree.insert(x)
    input_tree.draw()

    x = 25
    dist = 0
    print("dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 1
    print("dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 2
    print("dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 3
    print("dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))

    x = 20
    dist = 0
    print("dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 1
    print("dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 2
    print("dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 3
    print("dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 4
    print("dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))

    x = 50
    dist = 0
    print("dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 1
    print("dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 2
    print("dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 3
    print("dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 4
    print("dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 5
    print("dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))

    x = 22
    dist = 0
    print("dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 1
    print("dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 2
    print("dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 3
    print("dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 4
    print("dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 5
    print("dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 6
    print("dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
    dist = 7
    print("dist_k({},{})={}".format(x, dist, input_tree.find_dist_k(x, dist)))
