#Postorder Depth First Search
# Traverse tje left subtree
# traverse the right subtree
# visit the root


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printPostorder(root):
    #base case
    if root:
        printPostorder(root.left)
        printPostorder(root.right)

        print(root.val,end=" "),



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Postorder Traversal DFS")
printPostorder(root)
