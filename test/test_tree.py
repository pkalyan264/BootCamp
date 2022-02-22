from unittest import TestCase
from challenges.tree import Tree, Node


class TestBST(TestCase):

    def test_insert_func(self):
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
        self.assertEqual(tree.root.right.left.left.val, 25)

    def test_inorder_traversal(self):
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

