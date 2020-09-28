import numpy as np
NUMBER_OF_POINTS = 10
CO_RANGE = 10

class Node:
    def __init__(self, key, y):
        self.key = key
        self.y = y
        # -1 is one more on the left, 1 is one more on the right
        self.weight = 0
        self.right = None
        self.left = None
        self.parent = None

    def addChild(self, n):
        if n.key < self.key:
            if not self.left:
                self.left = n
            else:
                self.left.addChild(n)
        else:
            if not self.right:
                self.right = n
            else:
                self.right.addChild(n)
        n.parent = self

    def youngParent(self):
        if self.weight == 0 and self.parent:
            return self.parent.youngParent
        else:
            return self

    def heightAndWeight(self):
        if self.left:
            left_side = self.left.heightAndWeight
        else:
            left_side = 0
        if self.right:
            right_side = self.right.heightAndWeight
        else:
            right_side = 0

        self.weight = right_side - left_side
        return max(left_side, right_side) + 1

    def draw(self, mat):
        mat[self.key, self.y] = 1
        self.left.draw()
        self.right.draw()


class BST:
    def __init__(self):
        self.root = None

    def Insert(tree, node):
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

    def addChild(self, new_node):
        self.insert(new_node)
        yp_node = new_node.youngParent()
        yp_node.heightAndWeight()
        if yp_node.weight == 2 or yp_node.weight == -2:
            self.balance(yp_node)
            yp_node.heightAndWeight()
        else:
            # is needed?????? I don't think so but checking is needed
            self.root.heightAndWeight()

    def insert(self, new_node):
        if not self.root:
            self.root = new_node
        else:
            self.root.addChild(new_node)

    def balance(self, yp_node):
        pass

    def draw(self, mat):
        # recursion limit in python is 300, so dividing by 4
        if self.root:
            if self.root.left:
                if self.root.left.left:
                    self.root.left.left.draw
                if self.root.left.right:
                    self.root.left.right.draw
            if self.root.right:
                if self.root.right.left:
                    self.root.right.left.draw
                if self.root.right.right:
                    self.root.right.right.draw


def printPoints(tree):
    mat = np.zeros((CO_RANGE, CO_RANGE))
    tree.draw(mat)
    for cell in mat:
        if cell == 0:
            print(" ", end='')
        if cell == 1:
            print("O", end='')
        if cell == 2:
            print("|", end='')
        if cell == 3:
            print("X", end='')




def main():
    print("Where would you like to place the vertical line?")


if __name__ == '__main__':
    main()
