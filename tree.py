from node import Node
import unittest

class Tree:
    """ Tree class for binary tree """

    def __init__(self):
        """ Constructor for Tree class """
        self.root = None

    def getRoot(self):
        """ Method for get root of the tree """
        return self.root

    def add(self, data):
        """ Method for add data to the tree """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """Method for add data to the tree

        Args:
            data (int): data to add

        Returns:
            None
        """
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        """Method for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

    def deleteTree(self):
        """ Method for deleting a tree 
        
        Args:
            None

        Returns:
            None
        
        """
        self.root = None

    def printTree(self):
        """ Method for printing a tree (inorder traversal)
        
        Args:
            None

        Returns:
            None
        
        """
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node):
        """ Method for printing a tree's inorder traversal
        
        Args:
            none (Node): current Node

        Returns:
            None
        """
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        """ Method for printing a tree's preorder traversal
        
        Args:
            none (Node): current Node

        Returns:
            None
        """
        if node is not None:
            print(str(node.data) + ' ')
            self._printInorderTree(node.left)
            self._printInorderTree(node.right)

    def _printPostorderTree(self, node):
        """ Method for printing a tree's postorder traversal
        
        Args:
            none (Node): current Node

        Returns:
            None
        """
        if node is not None:
            self._printInorderTree(node.left)
            self._printInorderTree(node.right)
            print(str(node.data) + ' ')


class TestTreeFind(unittest.TestCase):
    def test_find_found(self):
        root = Tree()
        root.add(1)
        root.add(2)
        root.add(3)
        root.add(4)
        root.add(5)
        root.add(6)
        root.add(7)
        assert root.find(4) is not None
    
    def test_find_not_found(self):
        root = Tree()
        root.add(1)
        root.add(2)
        root.add(3)
        root.add(4)
        root.add(5)
        root.add(6)
        root.add(7)
        assert root.find(8) is None