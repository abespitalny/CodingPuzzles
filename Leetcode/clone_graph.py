'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
'''

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return str(self.val)

# Time: O(V+E), Space: O(V)
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        
        stack = [node]
        cloneNodesMap = {}

        while len(stack) != 0:
            originalNode = stack.pop()
            
            if originalNode not in cloneNodesMap:
                cloneNode = Node(originalNode.val)
                cloneNodesMap[originalNode] = cloneNode
            else:
                cloneNode = cloneNodesMap[originalNode]

            cloneNeighbors = []
            for i in originalNode.neighbors:
                if i not in cloneNodesMap:
                    cloneNeighbor = Node(i.val)
                    cloneNodesMap[i] = cloneNeighbor
                    stack.append(i)
                else:
                    cloneNeighbor = cloneNodesMap[i]
                cloneNeighbors.append(cloneNeighbor)

            cloneNode.neighbors = cloneNeighbors
        
        return cloneNodesMap[node]

# What follows is for testing purposes only!

def construct_graph(adjacenyList):
    if (adjacenyList is None) or (len(adjacenyList) == 0):
        return None
    
    graph = {(i + 1): Node(i + 1) for i in range(len(adjacenyList))}
    for i in range(len(adjacenyList)):
        node = graph[i + 1]
        node.neighbors = [graph[j] for j in adjacenyList[i]]
    return graph

def construct_adjacency_list(node):
    if node is None:
        return []

    adjDict = {}
    visited = set()
    stack = [node]

    while len(stack) != 0:
        currentNode = stack.pop()
        visited.add(currentNode)
        neighbors = []

        for i in currentNode.neighbors:
            neighbors.append(i.val)
            if i not in visited:
                stack.append(i)

        adjDict[currentNode.val] = neighbors

    adjList = [0]*len(adjDict)
    for i in adjDict:
        adjList[i - 1] = adjDict[i]
    return adjList

solution = Solution()

graph = construct_graph([[2,4],[1,3],[2,4],[1,3]])
cloneGraph = solution.cloneGraph(graph[1])
# Expected: [[2,4],[1,3],[2,4],[1,3]]
print(construct_adjacency_list(cloneGraph))

graph = construct_graph([[]])
cloneGraph = solution.cloneGraph(graph[1])
# Expected: [[]]
print(construct_adjacency_list(cloneGraph))

graph = construct_graph([])
cloneGraph = solution.cloneGraph(None)
# Expected: []
print(construct_adjacency_list(cloneGraph))
