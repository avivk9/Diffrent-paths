import random
VERTEXES = 8


def BFS(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = []
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.pop(0)
        for ind in range(len(graph[u])):
            if visited[ind] is False and graph[u][ind] > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return True if visited[t] else False


def FordFulkerson(graph, s, t):
    parent = [-1] * (len(graph))
    max_flow = 0
    while BFS(graph, s, t, parent):
        path_flow = float("Inf")
        end = t

        while end != s:
            # Find the minimum value in select path
            path_flow = min(path_flow, graph[parent[end]][end])
            end = parent[end]

        max_flow += path_flow
        v = t

        while v != s:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow


def diffrent_pathes(graph, s, t):
    for i in range(VERTEXES):
        for j in range(VERTEXES):
            if graph[i][j] != 0:
                graph[i][j] = 1
    return FordFulkerson(graph, s, t)



if __name__ == "__main__":
    rand = 0
    graph = [[0 for i in range(VERTEXES)] for j in range(VERTEXES)]
    for i in range(VERTEXES):
        for j in range(VERTEXES):
            rand = random.randint(0,1)
            if rand == 1:
                rand = random.randint(0, 50)
                graph[i][j] = rand
    s = random.randint(1, VERTEXES) - 1  # SOURCE
    t = random.randint(1, VERTEXES) - 1  # SINK
    print("The random graph: ")
    for i in range(VERTEXES):
        print(str(graph[i]))
    print("random v1 = " + str(s))
    print("random v2 = " + str(t))
    print("amount of diffrent pathes from v1 to v2: " + str(diffrent_pathes(graph, s, t)))


