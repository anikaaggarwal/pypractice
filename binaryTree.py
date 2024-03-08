#python class that represents individual node
#in a binary tree

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
#level order traversal or BFS:
    #finding height of tree. for each level, run a recursive
    #function by maintaining the current height. Whenever
    #the level of a node matches, print that node


def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)

def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

    if lheight > rheight:
        return lheight+1
    else:
        return rheight+1

def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printCurrentLevel(root, i)


#implementation of a simple binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

print("Binary Tree BFS/Level order Traversal")
printLevelOrder(root)
