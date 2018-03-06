from node import Node
from tree import Tree

class Calendar:
    def __init__(self):
        self.tree=Tree(None)
    
    def add(self, start, end, task=""):
        self.tree.insert(Node(start, end, task))
    
    def lookup(self, start, end):
        return self.tree.lookup(start, end)

    def delete(self, start, end):
        return self.tree.delete_interval(start, end)
