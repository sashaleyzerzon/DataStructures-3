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
class CoordinateNode:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.right = None
        self.left = None
        #self.p = None

class Node:
    def __init__(self,key):
        self.key = key
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






def main():
    pass

if __name__ == '__main__':
    main()
