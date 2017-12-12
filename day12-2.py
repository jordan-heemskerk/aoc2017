import re

pattern = re.compile(r"(\d+) <-> (.*)")

graph = {}
with open("input12.txt") as fh:
    for line in fh:
        vertex, neighbours = pattern.match(line).groups() 
        graph[vertex] = set(neighbours.split(", "))

def dfs(G, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(G[vertex] - visited)
    return visited


groups = 0
node_set = set(graph.keys())

while len(node_set) != 0:
    found_nodes = set(dfs(graph, node_set.pop()))
    node_set = node_set -  found_nodes
    groups += 1

print groups
