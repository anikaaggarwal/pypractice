#Preorder Traversal Depth First Search
# visit the root
# traverse the left subtree
# traverse the right subtree
#

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printPreorder(root):
    #base case
    if root:
        #print data of the root node
        print(root.val, end=" "),

        #then print left child
        printPreorder(root.left)

        #now print right child
        printPreorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Preorder Traversal DFS")
printPreorder(root)
