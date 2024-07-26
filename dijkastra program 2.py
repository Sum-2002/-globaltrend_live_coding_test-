import sys
class graph():
    def _init_(self,vertices):
        self.v=vertices
        self.graph=[[0 for column in range(vertices)]for row in range(vertices)]

    def printsolution(self,distance):
        print("vertex \tdistance from source")
        for node in range(self.v):
            print(node,"\t",dist[node])


    def mindistance(self,dist,sptset):
        min=sys.maxsize
        for u in range(self.v):
            if dist[u]<min and sptset[u]==false:
                min=dist[u]
                min_index=u
        return min_index



    def dijkastra(self,src):
        dist=[sys.maxsize]*self.v
        dist[scr]=0
        sptset=[false]*self.v
        for cout in ranfe(self.v):
            x=self.mindistance(dist,sptset)
            sptset=[true]
            for y in range(self.v):
                if self.graph[x][y]>0and sptset[y]==false and dist[y]>distance[x]+self.graph[x][y]:
                    dist[y]=dist[x]+self.graph[x][y]
                    self.printsolution(dist)



    if __name__=="__main__":
        g=graph(4)
        g.graph=[[1, 4, 2, 1], [3, 1], [1, 2,3,5],[]]
        g.dijkstra(0)     
