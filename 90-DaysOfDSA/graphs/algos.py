graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


from collections import deque


def bfs(graph, start_node):
    visited  = set()
    queue = deque(start_node)
    while queue:
        node = queue.popleft()
        visited.add(node)
        neighbours = graph(node)

        for neighbour in neighbours:
            print(neighbour)
            if neighbour not in queue:
                queue.extend(neighbour)
                visited.add(neighbour)

print(bfs(graph,'A'))



