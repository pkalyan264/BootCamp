class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root=None):
        self.root: Node = root

    def insert(self, key, curr_root=Node(None)):
        if curr_root is None:
            return Node(key)
        elif curr_root.val is None:
            return self.insert(key, self.root)
        else:
            if curr_root.val == key:
                return curr_root
            elif curr_root.val < key:
                curr_root.right = self.insert(key, curr_root.right)
            else:
                curr_root.left = self.insert(key, curr_root.left)
        return curr_root

    def inorder(self, curr_root=Node(None), tree_nodes=[]):
        if curr_root is None:
            return tree_nodes
        elif curr_root.val is None:
            return self.inorder(self.root, tree_nodes)
        else:
            self.inorder(curr_root.left, tree_nodes)
            tree_nodes.append(curr_root.val)
            self.inorder(curr_root.right, tree_nodes)
            return tree_nodes


if __name__ == '__main__':
    node = Node(50)
    tree = Tree(node)
    tree.insert(40)
    tree.insert(60)
    tree.insert(30)

    print(tree.inorder())
