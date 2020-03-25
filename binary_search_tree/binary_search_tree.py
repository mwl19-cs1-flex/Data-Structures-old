import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value and self.left == None:
            self.left = BinarySearchTree(value)
            # self.value.left.insert(value)
            # self.left = BinarySearchTree(value)
        elif value >= self.value and self.right == None:
            self.right = BinarySearchTree(value)
            # self.value.right.insert(value)
            # self.right = BinarySearchTree(value)
        elif value < self.value and self.left != None:
            self.left.insert(value)
        elif value >= self.value and self.right != None:
            self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        else:
            if target < self.value and self.left == None:
                return False
            elif target >= self.value and self.right == None:
                return False
            elif target < self.value and self.left != None:
                self.left.contains(target)
            elif target >= self.value and self.left != None:
                self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
