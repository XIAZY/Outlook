from node import Node

class Tree:
    # essentially an AVL tree implemantation
    def __init__(self, root):
        self.root = root

    def insert(self, new_node):
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
                right=node.right
                if (right.left_height() <= right.right_height()):
                    # single counter clockwise rotation
                    node=node.counter_clockwise_rotation().parent
                elif (right.left_height()>right.right_height()):
                    # need double rotation
                    right.clockwise_rotation()
                    node=node.counter_clockwise_rotation().parent
            elif (node.left_height() > node.right_height()+1):
                # left is taller by 2
                left=node.left
                if (left.left_height() >= left.right_height()):
                    # single clockwise rotation
                    node=node.clockwise_rotation().parent
                elif (left.left_height()<left.right_height()):
                    # need double rotation
                    left.counter_clockwise_rotation()
                    node=node.clockwise_rotation().parent
            if node.parent is None:
                self.root = node
            node=node.parent

