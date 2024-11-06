"""
Case #2. Exercise  3
@author: EDA Team
"""

# Classes provided by EDA Team
from avl import AVLTree
from bintree import BinaryNode
from bst import BinarySearchTree

"""
    Functions to support merge operation
"""


def __visit_node_and_insert(result: AVLTree, node: BinaryNode) -> None:
    if node is not None:
        __visit_node_and_insert(result, node.left)
        result.insert(node.elem)
        __visit_node_and_insert(result, node.right)


def __merge(t1: BinarySearchTree, t2: BinarySearchTree) -> BinarySearchTree:
    """gets two BST and creates a new tree containing the elements from t1 and t2"""
    res = AVLTree()
    __visit_node_and_insert(res, t1.root)
    __visit_node_and_insert(res, t2.root)
    return res


"""
    Functions to support intersection operation
"""


def __intersection_rec(res: AVLTree, node1: BinaryNode, node2: BinaryNode) -> None:
    """saves into the avl_tree the elements that are in both subtrees node1 and node2"""
    if node1 is None or node2 is None:
        return None

    if node1.elem == node2.elem:
        res.insert(node1.elem)
        __intersection_rec(res, node1.left, node2.left)
        __intersection_rec(res, node1.right, node2.right)
    elif node1.elem < node2.elem:
        __intersection_rec(res, node1, node2.left)
        __intersection_rec(res, node1.right, node2)
    else:
        __intersection_rec(res, node1, node2.right)
        __intersection_rec(res, node1.left, node2)


def __intersection(t1: BinarySearchTree, t2: BinarySearchTree) -> BinarySearchTree:
    """returns an AVL avl_tree containing the elements that are in trees t1 y t2"""
    res = AVLTree()
    __intersection_rec(res, t1.root, t2.root)
    return res


"""
    Function to support difference operation
"""


def __difference_rec(res: AVLTree, node1: BinaryNode, tree2: BinarySearchTree) -> None:
    """saves into avl_tree the elements from the subtree node1 that are not int tree2"""
    if not node1:
        return
    if not tree2.search(node1.elem):
        res.insert(node1.elem)
    __difference_rec(res, node1.left, tree2)
    __difference_rec(res, node1.right, tree2)


def __difference(t1: BinarySearchTree, t2: BinarySearchTree) -> BinarySearchTree:
    """returns an AVL tree containing the elements from the tree t1 that are not in t2"""
    res = AVLTree()
    __difference_rec(res, t1.root, t2)
    return res


def create_tree(tree1: BinarySearchTree, tree2: BinarySearchTree, opc: str) -> BinarySearchTree:
    # Valid opc names and their corresponding functions
    options = {"merge": __merge, "intersection": __intersection, "difference": __difference}

    # Perform and return directly the requested operation
    return options[opc](tree1, tree2)


# Some usage examples
if __name__ == '__main__':
    input_list = [50, 55, 54, 20, 60, 15, 18, 5, 25, 24, 75, 80]
    # input_list_01 = [5, 1, 7, 9, 23]
    # input_list_02 = [1, 9, 11, 23]

    # input_list_01 = [5, 12, 2, 1, 3, 9, 21, 23]
    input_list_01 = [5, 18, 1, 24]
    input_list_02 = [16, 18, 5, 1, 12]
    # input_list_01 = [50, 55, 54, 20, 0, 15, 18, 5, 25, 24, 75, 80]
    # input_list_02 = [60]

    # Build and draw first tree
    test_tree1 = BinarySearchTree()
    for x in input_list_01:
        test_tree1.insert(x)
    test_tree1.draw()

    # Build and draw second tree
    test_tree2 = BinarySearchTree()
    for x in input_list_02:
        test_tree2.insert(x)
    test_tree2.draw()

    function_names = ["merge", "intersection", "difference"]

    for op_name in function_names:
        test_res = create_tree(test_tree1, test_tree2, op_name)
        print(f"-- Result for {op_name} method. #{test_res.size()} nodes")
        test_res.draw()
