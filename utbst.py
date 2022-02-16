import BST
import unittest


class TestBST(unittest.TestCase):
    def test_node_initialiser(self):
        curr = BST.Tree(10)
        self.assertEqual(curr.val, 10)
        self.assertIsNone(curr.left)
        self.assertIsNone(curr.right)

        curr = BST.Tree()
        self.assertIsNone(curr.val)

    def test_Insert_Func(self):
        curr = BST.Tree(20)
        curr = curr.insert(10)
        curr = curr.insert(30)
        self.assertEqual(curr.val, 20)
        self.assertEqual(curr.left.val, 10)
        self.assertEqual(curr.right.val, 30)

        curr = BST.Tree(20)
        curr = curr.insert(30)
        curr = curr.insert(10)
        self.assertEqual(curr.val, 20)
        self.assertEqual(curr.left.val, 10)
        self.assertEqual(curr.right.val, 30)

        curr = BST.Tree(20)
        curr = curr.insert(40)
        curr = curr.insert(30)
        curr = curr.insert(25)
        self.assertEqual(curr.val, 20)
        self.assertEqual(curr.right.val, 40)
        self.assertEqual(curr.right.left.val, 30)
        self.assertEqual(curr.right.left.left.val, 25)

    def test_Inorder_Traversal(self):
        curr = BST.Tree(20)
        curr = curr.insert(10)
        curr = curr.insert(30)
        self.assertEqual(BST.Tree.inorder(curr, []), [10, 20, 30])

        curr = BST.Tree(20)
        curr = curr.insert(30)
        curr = curr.insert(10)
        self.assertEqual(BST.Tree.inorder(curr, []), [10, 20, 30])

        curr = BST.Tree(20)
        curr = curr.insert(40)
        curr = curr.insert(30)
        curr = curr.insert(25)
        self.assertEqual(BST.Tree.inorder(curr, []), [20, 25, 30, 40])


if __name__ == '__main__':
    unittest.main()
