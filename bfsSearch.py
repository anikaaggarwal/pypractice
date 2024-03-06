from collections import defaultdict

#class to represent a directed graph using adjacency lists
class Graph:

	#constructor
	def __init__(self):
		#default dictionary to store graph
		self.graph = defaultdict(list)
	#func to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	#func to print a BFS of graph
	def BFS(self, s):
		#marking all vertices as not visited
		visited = [False] * (max(self.graph) + 1)
		#creatign a queue for BFS
		queue = []
		#mark the source node as visited and enqueue it
		queue.append(s)
		visited[s] = True

		while queue:
			#dequeueing a vertex from queue and printing it
			s = queue.pop(0)
			print(s, end=" ")

			#getting all adjacent vertices of the dequeued vertex s.
			#if an adjacent has not been visited, then
			#mark it visited and enqueue it
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True


#creating a graph
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal"
		" (starting from vertex 0)")
g.BFS(0)
