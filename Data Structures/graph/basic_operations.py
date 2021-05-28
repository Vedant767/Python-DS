def find_path(graph, start, end, path=[]):
    path += [start]
    
    if start ==  end:
        return path
    
    for node in graph[start]:
        if node not in path:
            new = find_path(graph, node, end, path)
            
            if new:
                return path
    return None

def find_all_path(graph, start, end, path = []):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []  
    paths = []
    for node in graph[start]:
        if node not in path:
            newnode = find_all_path(graph, node, end, path)
            for new in newnode:
                paths.append(new)
    return paths


graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

print(find_all_path(graph, 'A', 'D'))