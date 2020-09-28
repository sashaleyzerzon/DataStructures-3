import numpy as np
from Lib.random import randrange

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
        self.line = False
        # TODO: check if needed to avoid deep recursion
        # self.height

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
            return self.parent.youngParent()
        else:
            return self

    def heightAndWeight(self):
        if self.left:
            left_side = self.left.heightAndWeight()
        else:
            left_side = 0
        if self.right:
            right_side = self.right.heightAndWeight()
        else:
            right_side = 0

        self.weight = right_side - left_side
        return max(left_side, right_side) + 1

    def draw(self, mat):
        mat[self.key, self.y] = 1
        if self.left:
            self.left.draw(mat)
        if self.right:
            self.right.draw(mat)

    def drawLine(self, mat):
        for cell in range(CO_RANGE):
            mat[cell, self.key] = 2


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
            pass
            # is needed?????? I don't think so but checking is needed
            # self.root.heightAndWeight()

    def insert(self, new_node):
        if not self.root:
            self.root = new_node
        else:
            self.root.addChild(new_node)

    def balance(self, yp_node):
        pass

    def draw(self, mat):
        # TODO: check if needed:
        # recursion limit in python is 300, so dividing by 4
        # if self.root:
        #     mat[self.root.y, self.root.key] = 1
        #     if self.root.left:
        #         mat[self.root.left.y, self.root.left.key] = 1
        #         if self.root.left.left:
        #             self.root.left.left.draw()
        #         if self.root.left.right:
        #             self.root.left.right.draw()
        #     if self.root.right:
        #         mat[self.root.right.y, self.root.right.key] = 1
        #         if self.root.right.left:
        #             self.root.right.left.draw()
        #         if self.root.right.right:
        #             self.root.right.right.draw()
        if self.root:
            self.root.draw(mat)


def Printer(mat):
    for line in mat:
        for cell in line:
            if cell == 0:
                print(" ", end=' ')
            if cell == 1:
                print("O", end=' ')
            if cell == 2:
                print("|", end=' ')
            if cell == 3:
                print("X", end=' ')
        print("")


def BuildTree():
    T = AVL()
    for n in range(NUMBER_OF_POINTS):
        n = Node(randrange(0, CO_RANGE + 1, 1), randrange(0, CO_RANGE + 1, 1))
        T.addChild(n)
    return T


def NearestRightPoint(T, x0):
    return None


def main():
    mat = np.zeros((CO_RANGE + 1, CO_RANGE + 1))
    T = BuildTree()
    T.draw(mat)
    Printer(mat)
    x0 = int(input("Where would you like to place the vertical line?"))
    # TODO: needs to be implemented inside the method NearestRightPoint
    # start
    the_line = Node(x0, 1)
    the_line.line = True
    T.addChild(the_line)
    the_line.drawLine(mat)
    Printer(mat)
    # end

    # TODO: uncomment after implementation
    # point = NearestRightPoint(T, x0)
    # mat[point.y, point.key] == 3


if __name__ == '__main__':
    main()
