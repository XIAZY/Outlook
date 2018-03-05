class Node:

    def __init__(self, lo, hi, task, height=0):
        self.lo = lo
        self.hi = hi
        self.task = task
        # the highest hi in the whole subtree
        self.max = hi
        # left and right children
        self.left = None
        self.right = None
        self.parent = None
        self.is_left_child_of_parent = None
        self.height = height

    def __lt__(self, other):
        if (self.lo < other.lo):
            return True
        elif (self.lo == other.lo and self.hi < other.hi):
            return True
        else:
            return False

    def __eq__(self, other):
        return self.lo == other.lo and self.hi == other.hi

    def __hash__(self):
        return hash((self.lo, self.hi))

    def counter_clockwise_rotation(self):
        # single c clockwise rotation
        x = self.right

        if (self.parent is not None):
            # self is not a root
            if (self.is_left_child_of_parent):
                # move x to self's parent's left child pos
                self.parent.left = x
                x.parent = self.parent
                x.is_left_child_of_parent = True
            else:
                # move x to self's parent's right child pos
                self.parent.right = x
                x.parent = self.parent
                x.is_left_child_of_parent = False
        else:
            # self is a root
            x.parent=None
            x.is_left_child_of_parent=None
        # move x.left to self.right
        self.right = x.left
        if (self.right is not None):
            self.right.parent = self
            self.right.is_left_child_of_parent = False
        # move self to x.left
        self.parent = x
        x.left = self
        self.is_left_child_of_parent=True
        self.update_height()
        x.update_height()
        return self

    def clockwise_rotation(self):
        # single c clockwise rotation
        x = self.left

        if (self.parent is not None):
            # self is not a root
            if (self.is_left_child_of_parent):
                # move x to self's parent's left child pos
                self.parent.left = x
                x.parent = self.parent
                x.is_left_child_of_parent = True
            else:
                # move x to self's parent's right child pos
                self.parent.right = x
                x.parent = self.parent
                x.is_left_child_of_parent = False
        else:
            # self is a root
            x.parent=None
            x.is_left_child_of_parent=None
        # move x.right to self.left
        self.left = x.right
        if (self.left is not None):
            self.left.parent = self
            self.left.is_left_child_of_parent = True
        # move self to x.right
        self.parent = x
        x.right = self
        self.is_left_child_of_parent=False
        self.update_height()
        x.update_height()
        return self

    def update_height(self):
        self.height = max(self.left_height(), self.right_height()) + 1

    def left_height(self):
        if (self.left is None):
            return -1
        else:
            return self.left.height

    def right_height(self):
        if (self.right is None):
            return -1
        else:
            return self.right.height
