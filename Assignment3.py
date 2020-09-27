#-------------------------------------------------------------------------------
# Name:        Tree
# Purpose:
#
# Author:      Alexandra Leyzerzon
#
# Created:     26/09/2020
# Copyright:   (c) Alexandra Leyzerzon 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Node:
    def __init__(self,key, y):
        self.key = key
        self.y = y
        # -1 is one more on the left, 1 is one more on the right
        self.weight = 0
        self.right = None
        self.left = None
        self.parent = None

class BST:
    def __init__(self):
        self.root = None
    def Insert(tree,node):
        y = None
        x = tree.root
        while x is not None:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        node.parent = y
        if y in None:
            tree.root = node
        else:
            if node.key < y.key:
                y.left = node
            else:
                y.right = node


class AVL:
    def __init__(self):
        self.root = None

    def insert(self, n):
        if not self.root:
            self.root = n
        else:
            pass

    def balance(self):
        pass

    def updateWeights(self):
        pass



def main():
    pass

if __name__ == '__main__':
    main()
