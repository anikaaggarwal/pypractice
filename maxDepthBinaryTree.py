#finding the height of the tree. height of a tree is the number of
# vertices in the tree from the root to the deepest node
#
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def maxDepth(node):
    if node is None:
        return 0
    else:
        ldepth = maxDepth(node.left)
        rdepth = maxDepth(node.right)

        #using the larger of the two to find max height of
        # the three
        if (ldepth > rdepth):
            return ldepth + 1
        else:
            return rdepth + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Height of the tree is %d" % (maxDepth(root)))
