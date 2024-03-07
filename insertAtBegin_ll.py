class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    #insert at beginning of the list
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node


    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

#creating a new linked list
llist = LinkedList()

#adding nodes to the linked list
llist.insertAtBegin('a')
llist.insertAtBegin('b')
llist.insertAtBegin('c')

print("Node Data")
llist.printLL()
