# -*- coding: utf-8 -*-
"""
Test battery, using unittest, to figure out some metrics about student's code
@author: EDA Team

If we can try to dynamically load the implementation files, the following could be useful together
with some way to get test_name value from argv

# Dynamic load of implementation files
import importlib

test_name = "exercise_01_final_gsg"
module = importlib.import_module(test_name)

"""

# Classes provided by EDA Team
from avl import AVLTree

# Test case support
import unittest

# Exercises implementation (the one used as reference, and the students one)
# Classes containing the different solutions
from phase2_p1 import BST2
# from phase2_1_isa import BST2
from phase2_p2 import create_tree
# from solution_with_iter import create_tree
# from solution_with_builtin_types import create_tree

"""
    Auxiliary functions to convert between types and more, if any
"""


class BST2_AVL(BST2, AVLTree):
    def nop(self):
        return


class Test(unittest.TestCase):
    # Provisional mark
    mark_exercise_01 = 0
    mark_exercise_02 = 0

    def test_zz_print_mark(self):
        print(f"*******************************")
        print(f"** Provisional mark E01 = {Test.mark_exercise_01}/14")
        print(f"** Provisional mark E02 = {Test.mark_exercise_02}/24")
        print(f"*******************************")

    def setUp(self):
        # As setUp is executed before each test, we separate initialization in two blocks
        if "_exercise01" in self._testMethodName:
            # Test Cases - Exercise 01
            # Cases: E01.01 .. E01.07
            self.tree01_description = BST2()

            self.tree01_elements = [14, 11, 18, 10, 13, 16, 19, 5, 12, 15, 17, 30, 4, 6, 29, 31, 2, 8, 24, 33, 1, 3, 7,
                                    9, 23, 25, 32, 34, 21, 27, 36, 20, 22, 26, 28, 35, 37]
            for x in self.tree01_elements:
                self.tree01_description.insert(x)

            # Cases: E01.08
            self.tree01_empty = BST2()

            # Cases: E01.09 .. E01.11
            self.tree01_size_1 = BST2()
            self.tree01_size_1.insert(1)

            # Cases: E01.11 .. E01.14
            self.tree01_avl = BST2_AVL()

            for i in range(1, 128):
                self.tree01_avl.insert(i)

        else:
            # Test Cases - Exercise 02
            # Cases: E02.20, E02.27, E02.34
            self.tree02_empty_1 = BST2()
            self.tree02_empty_2 = BST2()
            self.tree02_empty_res = BST2()

            # Cases: E02.21 .. E02.22, E02.28 .. E02.29, E02.35 .. E02.36
            self.tree02_1element_1 = BST2()
            self.tree02_1element_2 = BST2()
            self.tree02_1element_as_1 = BST2()

            self.tree02_1element_1.insert(1)
            self.tree02_1element_2.insert(2)
            self.tree02_1element_as_1.insert(1)

            # Cases: E02.23 .. E02.25, E02.30 .. E02.32, E02.37 .. E02.30
            self.tree02_nelement_1 = AVLTree()
            self.tree02_nelement_2 = AVLTree()
            self.tree02_nelement_as_1 = AVLTree()
            self.tree02_nelement_as_part_1 = AVLTree()
            self.tree02_nelement_as_complement_1 = AVLTree()

            for i in range(1, 128):
                self.tree02_nelement_1.insert(i)
                self.tree02_nelement_as_1.insert(i)

            for i in range(1, 65):
                self.tree02_nelement_as_part_1.insert(i)

            for i in range(65, 128):
                self.tree02_nelement_as_complement_1.insert(i)

            for i in range(301, 401):  # To avoid overlapping with _1 trees
                self.tree02_nelement_2.insert(i)

            # Cases: E02.26, E02.33, E02.40
            self.tree02_bad_balanced_1_l = BST2()
            self.tree02_bad_balanced_2_l = BST2()
            self.tree02_bad_balanced_1_r = BST2()
            self.tree02_bad_balanced_2_r = BST2()
            self.tree02_bad_balanced_3 = BST2()

            self.limit = 10  # This restricts the number of recursive calls depth, to get something "executable"
            for i in range(1, self.limit + 1):
                self.tree02_bad_balanced_1_r.insert(i)
                self.tree02_bad_balanced_2_r.insert(i)
                self.tree02_bad_balanced_3.insert(i * 100)

            for i in range(self.limit, 0, -1):
                self.tree02_bad_balanced_1_l.insert(i)
                self.tree02_bad_balanced_2_l.insert(i)

    def test_exercise01_test_01(self):
        print('Case E01.01: Exercise description. Test 01', end=" ")
        self.assertEqual(self.tree01_description.find_dist_k(30, 0), [30])
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise01_test_02(self):
        print('Case E01.02: Exercise description. Test 02', end=" ")
        self.assertEqual(sorted(self.tree01_description.find_dist_k(30, 2)), [18, 24, 33])
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise01_test_03(self):
        print('Case E01.03: Exercise description. Test 03', end=" ")
        self.assertEqual(sorted(self.tree01_description.find_dist_k(12, 6)), [2, 8, 15, 17, 30])
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise01_test_04(self):
        print('Case E01.04: Exercise description. Test 04', end=" ")
        self.assertEqual(sorted(self.tree01_description.find_dist_k(17, 7)), [4, 6, 23, 25, 32, 34])
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise01_test_05(self):
        print('Case E01.05: Exercise description. Test 05', end=" ")
        self.assertEqual(sorted(self.tree01_description.find_dist_k(26, 9)), [11, 15, 17, 36])
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise01_test_06(self):
        print('Case E01.06: Exercise description. Test 05 + k = 1000', end=" ")
        self.assertEqual(self.tree01_description.find_dist_k(30, 1000), [])
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise01_test_07(self):
        print('Case E01.07: Exercise description. Any number in the tree (no hardcoded!)', end=" ")
        self.assertEqual(sorted(self.tree01_description.find_dist_k(24, 3)), [19, 20, 22, 26, 28, 31])
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise01_test_08(self):
        print('Case E01.08: emptyTree', end=" ")
        self.assertEqual(self.tree01_empty.find_dist_k(1, 1), [])
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise01_test_09(self):
        print('Case E01.09: tree.size = 1 and n = 2 (not in the tree) and any k', end=" ")
        self.assertEqual(self.tree01_size_1.find_dist_k(2, 1), [])
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise01_test_10(self):
        print('Case E01.10: tree.size = 1 and n=1 and tree.root.elem = 1 and k = 0', end=" ")
        self.assertEqual(self.tree01_size_1.find_dist_k(1, 0), [1])
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise01_test_11(self):
        print('Case E01.11: tree.size = 1 and n=1 and tree.root.elem = 1 and k = 1', end=" ")
        self.assertEqual(self.tree01_size_1.find_dist_k(1, 1), [])
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise01_test_12(self):
        print('Case E01.12: AVL (size = 127, root.elem = 64), n = 64, k = 1000', end=" ")
        self.assertEqual(self.tree01_avl.find_dist_k(64, 1000), [])
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise01_test_13(self):
        print('Case E01.13: AVL (size = 127, root.elem = 64), n = 64, k = 1', end=" ")
        self.assertEqual(len(self.tree01_avl.find_dist_k(64, 1)), 2)
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise01_test_14(self):
        print('Case E01.14: AVL (size = 127, root.elem = 64), n = 64, k = 6', end=" ")
        self.assertEqual(len(self.tree01_avl.find_dist_k(64, 6)), 64)
        print('--> mark += 1')
        Test.mark_exercise_01 += 1

    def test_exercise02_test_20(self):
        print('Case E02.20: merge. 2 empty trees', end=" ")
        res = create_tree(self.tree02_empty_1, self.tree02_empty_2, "merge")
        self.assertEqual(res, self.tree02_empty_res)
        print('--> mark += 1')
        Test.mark_exercise_02 += 1

    def test_exercise02_test_21(self):
        print('Case E02.21: merge. 2 1-element trees. Both equal', end=" ")
        res = create_tree(self.tree02_1element_1, self.tree02_1element_as_1, "merge")
        self.assertEqual(res, self.tree02_1element_1)
        self.assertEqual(res, self.tree02_1element_as_1)
        print('--> mark += 1')
        Test.mark_exercise_02 += 1

    def test_exercise02_test_22(self):
        print('Case E02.22: merge. 2 1-element trees. Both different', end=" ")
        res = create_tree(self.tree02_1element_1, self.tree02_1element_2, "merge")
        self.assertNotEqual(res, self.tree02_1element_1)
        self.assertNotEqual(res, self.tree02_1element_2)
        self.assertEqual(res.size(), self.tree02_1element_1.size() + self.tree02_1element_2.size())
        print('--> mark += 1')
        Test.mark_exercise_02 += 1

    def test_exercise02_test_23(self):
        print('Case E02.23: merge. 2 n-elements trees. Both equal', end=" ")
        res = create_tree(self.tree02_nelement_1, self.tree02_nelement_as_1, "merge")
        self.assertEqual(res, self.tree02_nelement_1)
        self.assertEqual(res, self.tree02_nelement_as_1)
        print('--> mark += 1')
        Test.mark_exercise_02 += 1

    def test_exercise02_test_24(self):
        print('Case E02.24: merge. 2 n-elements trees. Both different', end=" ")
        res = create_tree(self.tree02_nelement_1, self.tree02_nelement_2, "merge")
        self.assertNotEqual(res, self.tree02_nelement_1)
        self.assertNotEqual(res, self.tree02_nelement_2)
        self.assertEqual(res.size(), self.tree02_nelement_1.size() + self.tree02_nelement_2.size())
        print('--> mark += 1')
        Test.mark_exercise_02 += 1

    def test_exercise02_test_25(self):
        print('Case E02.25: merge. 2 n-elements tree. Both partially equal', end=" ")
        res = create_tree(self.tree02_nelement_1, self.tree02_nelement_as_part_1, "merge")
        self.assertEqual(res, self.tree02_nelement_1)
        self.assertNotEqual(res, self.tree02_nelement_2)
        self.assertEqual(res.size(), self.tree02_nelement_1.size())
        print('--> mark += 1')
        Test.mark_exercise_02 += 1

    def test_exercise02_test_26(self):
        print(f"Case E02.26: merge. 2 very bad balanced trees. Check AVL (size={self.limit})", end=" ")
        res = create_tree(self.tree02_bad_balanced_1_l, self.tree02_bad_balanced_1_r, "merge")
        res_height = res.height()
        other_height = self.tree02_bad_balanced_1_r.height()
        # The AVL version has 6 levels for 100 elements
        self.assertLess(res_height, other_height)
        print(f" ({res_height}/{other_height} mark += 1)", end=" ")
        Test.mark_exercise_02 += 1
        # And sure that less than one of the input trees
        res = create_tree(self.tree02_bad_balanced_1_l, self.tree02_bad_balanced_3, "merge")
        res_height = res.height()
        other_height = self.tree02_bad_balanced_3.height()
        self.assertLess(res_height, other_height)
        print(f" ({res_height}/{other_height} mark += 1)")
        Test.mark_exercise_02 += 1

    def test_exercise02_test_27(self):
        print('Case E02.27: inter. 2 empty trees', end=" ")
        res = create_tree(self.tree02_empty_1, self.tree02_empty_2, "intersection")
        self.assertEqual(res, self.tree02_empty_res)
        print('--> mark += 1')
        Test.mark_exercise_02 += 1

    def test_exercise02_test_28(self):
        print('Case E02.28: inter. 2 1-element trees. Both equal', end=" ")
        res = create_tree(self.tree02_1element_1, self.tree02_1element_as_1, "intersection")
        self.assertEqual(res, self.tree02_1element_1)
        self.assertEqual(res, self.tree02_1element_as_1)
        print('--> mark += 1')
        Test.mark_exercise_02 += 1

    def test_exercise02_test_29(self):
        print('Case E02.29: inter. 2 1-element trees. Both different', end=" ")
        res = create_tree(self.tree02_1element_1, self.tree02_1element_2, "intersection")
        self.assertNotEqual(res, self.tree02_1element_1)
        self.assertNotEqual(res, self.tree02_1element_2)
        self.assertEqual(res, self.tree02_empty_res)
        self.assertEqual(res.size(), 0)
        print('--> mark += 1')
        Test.mark_exercise_02 += 1

    def test_exercise02_test_30(self):
        print('Case E02.30: inter. 2 n-elements trees. Both equal', end=" ")
        res = create_tree(self.tree02_nelement_1, self.tree02_nelement_as_1, "intersection")
        self.assertEqual(res, self.tree02_nelement_1)
        self.assertEqual(res, self.tree02_nelement_as_1)
        print('--> mark += 1')
        Test.mark_exercise_02 += 1

    def test_exercise02_test_31(self):
        print('Case E02.31: inter. 2 n-elements trees. Both different', end=" ")
        res = create_tree(self.tree02_nelement_1, self.tree02_nelement_2, "intersection")
        self.assertNotEqual(res, self.tree02_1element_1)
        self.assertNotEqual(res, self.tree02_1element_2)
        self.assertEqual(res, self.tree02_empty_res)
        self.assertEqual(res.size(), 0)
        print('--> mark += 1')
        Test.mark_exercise_02 += 1

    def test_exercise02_test_32(self):
        print('Case E02.32: inter. 2 n-elements tree. Both partially equal', end=" ")
        res = create_tree(self.tree02_nelement_1, self.tree02_nelement_as_part_1, "intersection")
        self.assertNotEqual(res, self.tree02_nelement_1)
        res_list = res.inorder_list()
        target_list = self.tree02_nelement_as_part_1.inorder_list()
        self.assertEqual(res_list, target_list)
        # TODO Next line is replaced by the above one
        # It is related with how trees are built? Only fails in recursive solution
        # One way to solve could be to have trees whose size is 2^x. It is done but it is still in fault!!
        # self.assertEqual(res, self.tree02_nelement_as_part_1)  # faulty line!
        self.assertEqual(res.size(), self.tree02_nelement_as_part_1.size())
        print('--> mark += 1')
        Test.mark_exercise_02 += 1

    def test_exercise02_test_33(self):
        print(f"Case E02.33: inter. 2 very bad balanced trees. Check AVL (size={self.limit})", end=" ")
        res = create_tree(self.tree02_bad_balanced_1_l, self.tree02_bad_balanced_1_r, "intersection")
        res_height = res.height()
        other_height = self.tree02_bad_balanced_1_r.height()
        # The AVL version has 6 levels for 100 elements
        self.assertLess(res_height, other_height)
        print(f" ({res_height}/{other_height} mark += 1)", end=" ")
        Test.mark_exercise_02 += 1
        # And sure that less than one of the input trees
        res = create_tree(self.tree02_bad_balanced_1_l, self.tree02_bad_balanced_3, "intersection")
        res_height = res.height()
        other_height = self.tree02_bad_balanced_3.height()
        self.assertLess(res_height, other_height)
        print(f" ({res_height}/{other_height} mark += 1)")
        Test.mark_exercise_02 += 1

    def test_exercise02_test_34(self):
        print('Case E02.34: diff. 2 empty trees', end=" ")
        res = create_tree(self.tree02_empty_1, self.tree02_empty_2, "difference")
        self.assertEqual(res, self.tree02_empty_res)
        print('--> mark += 1')
        Test.mark_exercise_02 += 1

    def test_exercise02_test_35(self):
        print('Case E02.35: diff. 2 1-element trees. Both equal', end=" ")
        res = create_tree(self.tree02_1element_1, self.tree02_1element_as_1, "difference")
        self.assertEqual(res, self.tree02_empty_res)
        print('--> mark += 1')
        Test.mark_exercise_02 += 1

    def test_exercise02_test_36(self):
        print('Case E02.36: diff. 2 1-element trees. Both different', end=" ")
        res = create_tree(self.tree02_1element_1, self.tree02_1element_2, "difference")
        self.assertEqual(res, self.tree02_1element_1)
        print('--> mark += 1')
        Test.mark_exercise_02 += 1

    def test_exercise02_test_37(self):
        print('Case E02.37: diff. 2 n-elements trees. Both equal', end=" ")
        res = create_tree(self.tree02_nelement_1, self.tree02_nelement_as_1, "difference")
        self.assertEqual(res, self.tree02_empty_res)
        print('--> mark += 1')
        Test.mark_exercise_02 += 1

    def test_exercise02_test_38(self):
        print('Case E02.38: diff. 2 n-elements trees. Both different', end=" ")
        res = create_tree(self.tree02_nelement_1, self.tree02_nelement_2, "difference")
        self.assertEqual(res, self.tree02_nelement_1)
        print('--> mark += 1')
        Test.mark_exercise_02 += 1

    def test_exercise02_test_39(self):
        print('Case E02.39: diff. 2 n-elements tree. Both partially equal', end=" ")
        res = create_tree(self.tree02_nelement_1, self.tree02_nelement_as_part_1, "difference")
        self.assertNotEqual(res, self.tree02_nelement_1)
        self.assertNotEqual(res, self.tree02_nelement_as_part_1)
        self.assertEqual(res.size(), self.tree02_nelement_1.size() - self.tree02_nelement_as_part_1.size())
        self.assertEqual(res, self.tree02_nelement_as_complement_1)
        print('--> mark += 1')
        Test.mark_exercise_02 += 1

    def test_exercise02_test_40(self):
        print(f"Case E02.40: diff. 2 very bad balanced trees. Check AVL (size={self.limit})", end=" ")
        res = create_tree(self.tree02_bad_balanced_1_l, self.tree02_bad_balanced_1_r, "difference")
        res_height = res.height()
        other_height = self.tree02_bad_balanced_1_r.height()
        # The AVL version has 6 levels for 100 elements
        self.assertLess(res_height, other_height)
        print(f" ({res_height}/{other_height} mark += 1)", end=" ")
        Test.mark_exercise_02 += 1
        # And sure that less than one of the input trees
        res = create_tree(self.tree02_bad_balanced_1_l, self.tree02_bad_balanced_3, "difference")
        res_height = res.height()
        other_height = self.tree02_bad_balanced_3.height()
        self.assertLess(res_height, other_height)
        print(f" ({res_height}/{other_height} mark += 1)")
        Test.mark_exercise_02 += 1


# Some usage examples
if __name__ == '__main__':
    unittest.main()
