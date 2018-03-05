from node import Node


class Tree:
    # essentially an AVL tree implemantation
    def __init__(self, root):
        self.root = root

    def insert(self, new_node):
        if self.root is None:
            self.root = new_node
            return new_node
        node = self.root
        while (node is not None):
            if (node == new_node):
                # same node, just replace the value
                node.task = new_node.task
                return node
            else:
                if new_node < node:
                    left = node.left
                    if left is None:
                        new_node.parent = node
                        new_node.is_left_child_of_parent = True
                        node.left = new_node
                        self.rebalance(node)
                        return new_node
                    else:
                        node = left
                elif new_node > node:
                    right = node.right
                    if right is None:
                        new_node.parent = node
                        new_node.is_left_child_of_parent = False
                        node.right = new_node
                        self.rebalance(node)
                        return new_node
                    else:
                        node = right

    def rebalance(self, start_node):
        # trace up and fix balance
        node = start_node
        while node is not None:
            # update the height
            node.update_height()
            if (node.left_height() + 1 < node.right_height()):
                # right is taller by 2
                right = node.right
                if (right.left_height() <= right.right_height()):
                    # single counter clockwise rotation
                    node = node.counter_clockwise_rotation().parent
                elif (right.left_height() > right.right_height()):
                    # need double rotation
                    right.clockwise_rotation()
                    node = node.counter_clockwise_rotation().parent
            elif (node.left_height() > node.right_height()+1):
                # left is taller by 2
                left = node.left
                if (left.left_height() >= left.right_height()):
                    # single clockwise rotation
                    node = node.clockwise_rotation().parent
                elif (left.left_height() < left.right_height()):
                    # need double rotation
                    left.counter_clockwise_rotation()
                    node = node.clockwise_rotation().parent
            if node.parent is None:
                self.root = node
            node = node.parent

    def lookup(self, lo, hi):
        node = self.root
        while node is not None:
            # three cases of overlap: 
            # node's lo inside given interval,
            # node's hi inside given interval,
            # interval inside node
            if (lo < node.lo < hi) or (lo < node.hi < hi) or (node.lo <= lo and node.hi >= hi):
                # overlap
                return False
            else:
                if node.left is None:
                    node = node.right
                elif node.left.max < lo:
                    # no possibility on left, go right
                    node = node.right
                else:
                    # lo <= node.left.max, go left
                    node = node.left
        return True

    def delete_node(self, node):
        if (node.left is None and node.right is None):
            parent = node.parent
            if parent is not None:
                if (node.is_left_child_of_parent):
                    parent.left = None
                else:
                    parent.right = None
                self.rebalance(parent)
            else:
                # node is root
                self.root=None
        elif (node.left is not None and node.right is None):
            parent = node.parent
            if (parent is not None):
                if node.is_left_child_of_parent:
                    parent.left = node.left
                else:
                    node.right = node.left
                node.left.parent = parent
                node.left.is_left_child_of_parent = node.is_left_child_of_parent
                self.rebalance(parent)
            else:
                self.root = node.left

        elif (node.left is None and node.right is not None):
            parent = node.parent
            if (parent is not None):
                if node.is_left_child_of_parent:
                    parent.left = node.right
                else:
                    node.right = node.right
                node.right.parent = parent
                node.right.is_left_child_of_parent = node.is_left_child_of_parent
                self.rebalance(parent)
            else:
                self.root = node.right

        else:
            # both children not empty
            # get the left most child of right subtree
            replacement = node.right
            replacement_parent = node
            while replacement.left is not None:
                replacement_parent = replacement
                replacement = replacement.left

            if replacement == node.right:
                # replace replacement_parent to replacement
                replacement_parent.right=None
                replacement_parent.replace(replacement)
                self.rebalance(replacement)
            else:
                # clean replacement's old parent
                replacement.replace(replacement.right)
                replacement.right=None
                node.replace(replacement)
                self.rebalance(replacement_parent)
            # # replace replacement to node
            # replacement.parent = node.parent
            # replacement.is_left_child_of_parent = node.is_left_child_of_parent
            # replacement.left = node.left
            # replacement.right = node.right
            # if (node.parent is not None):
            #     if (node.is_left_child_of_parent):
            #         node.parent.left = replacement
            #     else:
            #         node.parent.right = replacement
            # else:
            #     self.root = replacement
            
            # self.rebalance(replacement_parent)
