import task1

def BFS(V, G, n, e):
    
    fw = open('output2.txt','w')
    # initialize empty queue
    q = []
    # make starting node visited
    V[int(n)-1] = 1
    # enqueue node
    q.append(n)
    
    fw.write("Places: ")
    
    # continue while queue not empty 
    while len(q) != 0:
        # dequeue node
        m = q.pop(0)
        fw.write(str(m)+" ")
        # break loop if current node == end point 
        if int(m) == int(e):
            break
        
        # visit all neighbours of current node
        # and enqueue
        # 0----> not visited , 1-----> visited
        for neighbour in G[int(m)]:
            if  V[int(neighbour)-1] == 0:
                V[int(neighbour)-1] = 1
                q.append(neighbour)
                
#--------- Tester code----------------------
# create [0] array                 
visited = [0] * task1.total
graph = task1.graph
node = '1'
endPoint = '12'
BFS(visited , graph , node , endPoint)