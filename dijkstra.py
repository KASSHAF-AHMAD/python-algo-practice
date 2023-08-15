import heapq

infinity = 9999999
liSt = []

def dijkstra(Graph, source):
    dist = [infinity] * (vertex)
    v = source - 1
    dist[v] = 0
    prev = [None] * (vertex)
    visited = [False] * (vertex)

    opt = not Graph

    if opt != False:
        return dist, prev
    else:
        for v in Graph:
            heapq.heappush(liSt, (dist[int(v) - 1], int(v)))

        opt = not liSt

        while opt == False:
            hep = heapq.heappop(liSt)
            opt = not liSt

            if visited[hep[1] - 1]:
                continue
            visited[hep[1] - 1] = True

            if str(hep[1]) in Graph.keys():
                m = Graph[str(hep[1])]

                for v in range(len(m)):
                    push = dist[hep[1] - 1] + m[v][1]
                    if dist[int(m[v][0]) - 1] > push:
                        dist[int(m[v][0]) - 1] = push
                        prev[int(m[v][0]) - 1] = hep[1]
                        heapq.heappush(liSt, (dist[int(m[v][0]) - 1], int(m[v][0])))
        return dist, prev

input = open(r'input2.txt', 'r')
a = input.readline()

final = ""

for i in range(int(a)):
    a = input.readline()
    data = a.split(" ")
    vertex = int(data[0])
    path = int(data[1])
    
    listMaking = {}

    j = 0
    while j<path:
        line = input.readline()
        data1 = line.split(" ")
        source = data1[0]
        destination = data1[1]
        line = int(data1[2])

        if source in listMaking.keys():
            temp = listMaking[source]
            listMaking[source].append((destination, line))
        else:
            listMaking[source] = [(destination, line)]
        j = j + 1

    a = dijkstra(listMaking, 1)
    prev = a[1]

    if len(prev) == 1:
        t = str(vertex)
    else:
        y = [vertex]

        def iterate(prev, vertex, y):
            v = vertex - 1
            if prev[v] == None:
                return
            y.append(prev[v])
            vertex = prev[v]
            iterate(prev, vertex, y)

        iterate(prev, vertex, y)
        t = ""

        for k in range(len(y) - 1, -1, -1):
            t += str(y[k]) + " "
    final += t + "\n"

file = open(r'output2.txt', 'w')
file.write(final)