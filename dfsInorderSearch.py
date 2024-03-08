#inorder depth first search
# traverse the left subtree
# visit the root
# traverse the right subtree
#
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printInorder(root):
    if root:
        #first recur on left child
        printInorder(root.left)
        #printing data of node
        print(root.val, end=" ")

        #recur on right child
        printInorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder Traversal DFS")
printInorder(root)
