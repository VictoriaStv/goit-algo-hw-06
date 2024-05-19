import networkx as nx

def dfs(graph, start, end, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = dfs(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

def bfs(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next_node in graph.neighbors(vertex):
            if next_node not in path:
                if next_node == end:
                    yield path + [next_node]
                else:
                    queue.append((next_node, path + [next_node]))


G = nx.Graph()
ukrainian_personalities = ["Тарас Шевченко", "Леся Українка", "Іван Франко", "Михайло Грушевський", "Олександр Довженко"]
G.add_nodes_from(ukrainian_personalities)
G.add_edges_from([
    ("Тарас Шевченко", "Леся Українка"),
    ("Тарас Шевченко", "Іван Франко"),
    ("Тарас Шевченко", "Михайло Грушевський"),
    ("Леся Українка", "Іван Франко"),
    ("Леся Українка", "Михайло Грушевський"),
    ("Іван Франко", "Михайло Грушевський"),
    ("Іван Франко", "Олександр Довженко"),
    ("Михайло Грушевський", "Олександр Довженко")
])

# Шяхи DFS
print("DFS шляхи:")
for path in dfs(G, "Тарас Шевченко", "Олександр Довженко"):
    print(path)

# Шляхи BFS
print("\nBFS шляхи:")
for path in bfs(G, "Тарас Шевченко", "Олександр Довженко"):
    print(path)
