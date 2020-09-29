import numpy as np
import Lib.random as rd

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
        print(self.key)
        mat[round(self.y), round(self.key)] = round(self.key, 2)
        if self.left:
            self.left.draw(mat)
        if self.right:
            self.right.draw(mat)

    def drawLine(self, mat):
        for cell in range(CO_RANGE):
            mat[cell, round(self.key)] = -1


class AVL:
    def __init__(self):
        self.root = None

    def addChild(self, new_node):
        self.insert(new_node)
        yp_node = new_node.youngParent()  # yp_node == A
        yp_node.heightAndWeight()

        if yp_node.weight == 2 or yp_node.weight == -2:
            self.balance(yp_node)
            yp_node.heightAndWeight()

    def insert(self, new_node):
        if not self.root:
            self.root = new_node
        else:
            self.root.addChild(new_node)

    def balance(self, yp_node):
        if yp_node.weight == -2:
            # left
            next_node = yp_node.left
            if next_node.weight == 1:
                # left-right
                self.leftRotate(next_node)
            # left-left, and also the second phase of left-right
            self.rightRotate(yp_node)
        else:
            # right
            next_node = yp_node.right  # next_node == B
            if next_node.weight == -1:
                # right-left
                self.rightRotate(next_node)
            # right-right, and also the second phase of right-left
            self.leftRotate(yp_node)

    def leftRotate(self, A):
        # A is old_source
        B = A.right  # new source
        C = B.left  # old source's new right child
        D = A.parent  # ancestor parent, if exists

        B.left = A  # start rotation
        A.right = C
        A.parent = B
        B.parent = D
        if C:
            C.parent = A

        # change ancestor parent
        if D:
            if D.left == A:
                D.left = B
            else:
                D.right = B
        else:
            self.root = B

    def rightRotate(self, A):
        # A is old_source
        B = A.left  # new source
        C = B.right  # old source's new left child
        D = A.parent  # ancestor parent, if exists

        B.right = A  # start rotation
        A.left = C
        A.parent = B
        B.parent = D
        if C:
            C.parent = A
        # change ancestor parent or ake root
        if D:
            if D.left == A:
                D.left = B
            else:
                D.right = B
        else:
            self.root = B


def Printer(mat):
    for line in mat:
        for cell in line:
            if cell == 0:
                print("   ", end=' ')
            else:
                if cell == -1:
                    print(" | ", end=' ')
                else:
                    print(cell, end=' ')
        print("\n")


def BuildTree():
    T = AVL()
    for i in range(NUMBER_OF_POINTS):
        n = Node(rd.uniform(0, CO_RANGE), rd.uniform(0, CO_RANGE))
        T.addChild(n)
    return T


def NearestRightPoint(T, x0):
    return None


def main():
    mat = np.zeros((CO_RANGE + 1, CO_RANGE + 1))
    T = BuildTree()
    T.root.draw(mat)
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
