from Challenges.tree import Tree
import unittest
from Challenges.tree import Node


class TestBST(unittest.TestCase):
    def test_node_initializer(self):
        node = Node(10)
        tree = Tree(node)
        self.assertEqual(tree.root.val, 10)
        self.assertIsNone(tree.root.right)
        self.assertIsNone(tree.root.left)

        tree = Tree()
        self.assertIsNone(tree.root)

    def test_Insert_Func(self):
        node = Node(20)
        tree = Tree(node)
        tree.insert(10)
        tree.insert(30)
        self.assertEqual(tree.root.val, 20)
        self.assertEqual(tree.root.right.val, 30)
        self.assertEqual(tree.root.left.val, 10)

        node = Node(20)
        tree = Tree(node)
        tree.insert(30)
        tree.insert(10)
        self.assertEqual(tree.root.val, 20)
        self.assertEqual(tree.root.right.val, 30)
        self.assertEqual(tree.root.left.val, 10)

        node = Node(20)
        tree = Tree(node)
        tree.insert(40)
        tree.insert(30)
        tree.insert(25)
        self.assertEqual(tree.root.val, 20)
        self.assertEqual(tree.root.right.val, 40)
        self.assertEqual(tree.root.right.left.val, 30)
        self.assertEqual(tree.root.right.left.left.val,25)

    def test_Inorder_Traversal(self):
        node = Node(10)
        tree = Tree(node)
        tree.insert(20)
        tree.insert(30)
        self.assertEqual(tree.inorder(), [10, 20, 30])

        node = Node(20)
        tree = Tree(node)
        tree.insert(40)
        tree.insert(30)
        tree.insert(25)
        self.assertEqual(tree.inorder(tree_nodes=[]), [20, 25, 30, 40])

