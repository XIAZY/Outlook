class Node:

    def __init__(self, lo, hi, task_name):
        self.lo = lo
        self.hi = hi
        self.task_name = task_name
        # the highest hi in the whole subtree
        self.max = hi
        # left and right children
        self.left = None
        self.right = None

    def __lt__(self, other):
        if (self.lo < other.get_lo):
            return True
        elif (self.lo == other.get_lo and self.hi<other.get_hi):
            return True
        else:
            return False
    
    def __eq__(self, other):
        return self.lo == other.get_lo and self.hi == other.get_hi
        
    def get_lo(self):
        return self.lo
    
    def get_hi(self):
        return self.hi
    def set_left(self, left_node):
        self.left = left_node

    def get_left(self):
        return self.left

    def set_right(self, right_node):
        self.right = right_node

    def get_right(self):
        return self.right
