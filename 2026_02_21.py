#binary tree

#each node atmost 2 children

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)

## Tree Traversals
"""
# inorder traversal
def inorder(node):
    if node:
        inorder(node.left)
        print(node.value)
        inorder(node.right)

# prerder traversal
def preorder(node):
    if node:
        print(node.value)
        preorder(node.left)
        preorder(node.right)

# postorder traversal
def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(8)
root.right.left = Node(6)
root.right.right = Node(7)
inorder(root)
print("++++++++++++++++++++++++++++++++")
preorder(root)
print("++++++++++++++++++++++++++++++++")
postorder(root)
print("++++++++++++++++++++++++++++++++")
"""
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)
    
    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)
    
    def search(self, value):
        node = self.root
        while node:
            if value == node.value:
                return True
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return False


arr = [9, 2, 1, 10, 5, 8, 3]
bst = BinarySearchTree()
for i in arr:
    bst.insert(i)

print(bst.search(11))


def count_nodes(bst):
    node = bst.root
    count = 1
    n = 2
    while node:
        if node.left:
            count = count + 2**n
        n+=1
    return count
        