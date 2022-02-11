class TreeNode:
	def __init__(self,val=None):
		self.val=val
		self.left=None
		self.right=None
def insert(root, key):
	if root is None:
		return TreeNode(key)
	else:
		if root.val==key:
			return root
		elif root.val<key:
			root.right=insert(root.right,key)
		else:
			root.left=insert(root.left,key)
	return root

def inorder(root,lst):
	if root:
		inorder(root.left,lst)
		lst.append(root.val)
		inorder(root.right,lst)
	return lst

if __name__=='__main__':
	Tree=TreeNode(50)
	Tree=insert(Tree,40)
	Tree=insert(Tree,60)
	Tree=insert(Tree,30)

	lst=[]
	print(inorder(Tree,lst))



