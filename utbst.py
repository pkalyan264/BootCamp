import BST
import unittest

class TestBST(unittest.TestCase):
	def test_Node_Initialiser(self):
		treeNode=BST.TreeNode(10)
		self.assertEqual(treeNode.val,10)
		self.assertIsNone(treeNode.left)
		self.assertIsNone(treeNode.right)

	def test_Node_Initialiser(self):
		treeNode=BST.TreeNode()
		self.assertIsNone(treeNode.val)

	def test_Insert_Func(self):
		treeNode = BST.TreeNode(20)
		treeNode=  BST.insert(treeNode,10)
		treeNode=	BST.insert(treeNode,30)
		self.assertEqual(treeNode.val,20)
		self.assertEqual(treeNode.left.val,10)
		self.assertEqual(treeNode.right.val,30)

		treeNode = BST.TreeNode(20)
		treeNode=  BST.insert(treeNode,30)
		treeNode=	BST.insert(treeNode,10)
		self.assertEqual(treeNode.val,20)
		self.assertEqual(treeNode.left.val,10)
		self.assertEqual(treeNode.right.val,30)

		treeNode = BST.TreeNode(20)
		treeNode=  BST.insert(treeNode,40)
		treeNode=	BST.insert(treeNode,30)
		treeNode= BST.insert(treeNode,25)
		self.assertEqual(treeNode.val,20)
		self.assertEqual(treeNode.right.val,40)
		self.assertEqual(treeNode.right.left.val,30)
		self.assertEqual(treeNode.right.left.left.val,25)

	def test_Inorder_Traversal(self):
		treeNode = BST.TreeNode(20)
		treeNode=  BST.insert(treeNode,10)
		treeNode=	BST.insert(treeNode,30)
		self.assertEqual(BST.inorder(treeNode,[]),[10,20,30])

		treeNode = BST.TreeNode(20)
		treeNode=  BST.insert(treeNode,30)
		treeNode=	BST.insert(treeNode,10)
		self.assertEqual(BST.inorder(treeNode,[]),[10,20,30])		

		treeNode = BST.TreeNode(20)
		treeNode=  BST.insert(treeNode,40)
		treeNode=	BST.insert(treeNode,30)
		treeNode= BST.insert(treeNode,25)
		self.assertEqual(BST.inorder(treeNode,[]),[20,25,30,40])

if __name__=='__main__':
	unittest.main()

