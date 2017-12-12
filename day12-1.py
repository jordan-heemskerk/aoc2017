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

print len(dfs(graph, "0"))
