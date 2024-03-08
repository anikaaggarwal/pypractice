#level order traversal or bfs using queue
# we need to visit the nodes in a lower level before any
# node in a higher level, like a queue.
# 1. push the nodes of the lower level in the queue
# 2. when any node is visited, pop that node from the queue
# 3. and push the child of that node in the queue


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

#printing height of tree iteratively
def printLevelOrder(root):
    #base case
    if root is None:
        return

    #create empty queue
    queue = []

    #enqueue root and intiialise height
    queue.append(root)

    while(len(queue) > 0):
        #print front of queue and remove it from tree
        print(queue[0].data, end=" ")
        node= queue.pop(0)

        #enqueue left child
        if node.left is not None:
            queue.append(node.left)

        #enqueue right child
            if node.right is not None:
                queue.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level order traversal of binary tree")
printLevelOrder(root)




























# --- old code

#from collections import defaultdict

# #class to represent a directed graph using adjacency lists
# class Graph:

# 	#constructor
# 	def __init__(self):
# 		#default dictionary to store graph
# 		self.graph = defaultdict(list)
# 	#func to add an edge to graph
# 	def addEdge(self, u, v):
# 		self.graph[u].append(v)

# 	#func to print a BFS of graph
# 	def BFS(self, s):
# 		#marking all vertices as not visited
# 		visited = [False] * (max(self.graph) + 1)
# 		#creatign a queue for BFS
# 		queue = []
# 		#mark the source node as visited and enqueue it
# 		queue.append(s)
# 		visited[s] = True

# 		while queue:
# 			#dequeueing a vertex from queue and printing it
# 			s = queue.pop(0)
# 			print(s, end=" ")

# 			#getting all adjacent vertices of the dequeued vertex s.
# 			#if an adjacent has not been visited, then
# 			#mark it visited and enqueue it
# 			for i in self.graph[s]:
# 				if visited[i] == False:
# 					queue.append(i)
# 					visited[i] = True


# #creating a graph
# g = Graph()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)

# print("Following is Breadth First Traversal"
# 		" (starting from vertex 0)")
# g.BFS(0)
