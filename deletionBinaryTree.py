#starting at the root, find the deepest and rightmost node in the
#binary tree and the node which we want to delete
#2 replace the deepest rightmost node's data with the node to be
# deleted
# 3 delete deepest rightmost node
#

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#inorder traversal
def inorder(temp):
    if(not temp):
        return
    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)

# function to delete the given deppest node (d_node) in binary tree
def deleteDeepest(root, d_node):
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)

    #function to delete element in binary tree

def deletion(root, key):
    if root is None:
        return None
    if root.left is None and root.right is None:
        if root.key is key:
            return None
        else:
            return root
    key_node = None
    q = []
    q.append(root)
    temp = None
    while(len(q)):
        temp = q.pop(0)
        if temp.data is key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)
    if key_node:
        x = temp.data
        deleteDeepest(root, temp)
        key_node.data = x
    return root

root = Node(10)
root.left = Node(11)
root.left.left = Node(12)
root.left.right = Node(13)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)

print("Tree before deletion", end=" ")
inorder(root)
key = 12
root = deletion(root, key)
print();
print("the tree after deletion", end=" ")
inorder(root)
