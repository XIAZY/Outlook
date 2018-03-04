class Node:

    def __init__(self, lo, hi, task_name, parent=None, height=0):
        self.lo = lo
        self.hi = hi
        self.task_name = task_name
        # the highest hi in the whole subtree
        self.max = hi
        # left and right children
        self.left = None
        self.right = None
        self.parent=parent
        self.height=height

    def __lt__(self, other):
        if (self.lo < other.get_lo):
            return True
        elif (self.lo == other.get_lo and self.hi < other.get_hi):
            return True
        else:
            return False

    def __eq__(self, other):
        return self.lo == other.get_lo and self.hi == other.get_hi

    def __hash__(self):
        return hash((self.lo, self.hi))
