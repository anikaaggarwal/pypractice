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

    #add a node at any index when index starts from 0
    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while(current_node != None and position+1 != index):
                position += 1
                current_node = current_node.next

            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("index not founnd")

    #insert data at the end of the list
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    #update value of a node at a specific position
    def updateNode(self, value, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = value
        else:
            while(current_node != None and position != index):
                position += 1
                current_node = current_node.next

            if current_node != None:
                current_node.data = value
            else:
                print("Index not found")

    #Printing the linked list
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next

    def removeFirstNode(self):
        if self.head is None:
            return
        self.head = self.head.next

    def removeLastNode(self):
        if self.head is None:
            return
        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next
        current_node.next = None

    def removeAtIndex(self, index):
        if self.head is None:
            return
        current_node = self.head
        position = 0
        if position is index:
            self.removeFirstNode()
        else:
            while(current_node != Node and position+1 != index):
                position += 1
                current_node = current_node.next
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not found")

    def removeNode(self, data):
        current_node = self.head

        if current_node is data:
            self.removeFirstNode
            return
        while(current_node != None and current_node.next.data != data):
            current_node = current_node.next

        if current_node is None:
            return
        else:
            current_node.next = current_node.next.next

    def sizeOfList(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size += 1
                current_node = current_node.next
            return size
        else:
            return 0


#creating a new linked list
llist = LinkedList()

#adding nodes to the linked list
llist.insertAtBegin('a')
llist.insertAtEnd('aa')
llist.insertAtBegin('b')
llist.insertAtEnd('c')
llist.insertAtIndex('g', 2)

llist.updateNode('z', 0)

print("Node Data")
llist.printLL()

print("Removing first node")

llist.removeFirstNode()
llist.printLL()

print("Removing last node")
llist.removeLastNode()
llist.printLL()

print("Removing node at specified index")
llist.removeAtIndex(1)
llist.printLL()
print("Removing node at specified index AGAIN")
llist.removeAtIndex(1)
llist.printLL()

print("Size of the linked list")
print(llist.sizeOfList())
