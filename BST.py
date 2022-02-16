
class Tree:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, key):
        if self is None:
            return Tree(key)
        else:
            if self.val == key:
                return self
            elif self.val < key:
                self.right = Tree.insert(self.right, key)
            else:
                self.left = Tree.insert(self.left, key)
        return self

    def inorder(self, return_list):
        if self:
            Tree.inorder(self.left, return_list)
            return_list.append(self.val)
            Tree.inorder(self.right, return_list)
        return return_list


if __name__ == '__main__':
    curr = Tree(50)
    curr = curr.insert(40)
    curr = curr.insert(60)
    curr = curr.insert(30)

    lst = []
    print(Tree.inorder(curr, lst))
