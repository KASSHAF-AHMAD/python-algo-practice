import task1

def DFS_VISIT(G, n):
    visited[int(n)-1] = 1
    printed.append(n)
    
    for neighbour in G[n]:
        if neighbour not in visited:
            DFS_VISIT(G, neighbour)
    
    return printed
            
def DFS(G, end):
    fw = open('output3.txt','w')
    fw.write("Places: ")
    DFS_list = []
    
    for n in G:
        if n not in visited:
            DFS_list = DFS_VISIT(G, n)
            
    for i in range(len(DFS_list)):
        if str(DFS_list[i]) == end:
            fw.write(str(DFS_list[i])+" ")
            break
        else:
            fw.write(str(DFS_list[i])+" ")

    fw.close()                       
#------------- Tester Code---------------------
#  Create [0] array 
visited = [0] * task1.total
printed = []
graph = task1.graph
endPoint = '12'
DFS(graph, endPoint)