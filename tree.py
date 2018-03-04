from node import Node

class Tree:
    # essentially an AVL tree implemantation
    def __init__(self, root):
        self.root = root
    
    def insert(self, new_node):
        node = self.root
        while (node is not None):
            if (node == new_node):
                node.set_task = new_node.get_task()
                return node
            else:
                if new_node < node:
                    left = node.get_left()
                    if left == None:
                        node.set_left(new_node)
                        return node.get_left
                    else:
                        node = left
                elif new_node > node:
                    right = node.get_left()
                    if right == None:
                        node.set_right(new_node)
                        return node.get_right
                    else:
                        node = right
        
