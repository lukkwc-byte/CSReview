class Graph():
    def __init__(self, nodeDict):
        self.nodes=nodeDict

    def __str__(self):
        return str(self.nodes)
        
    def BFS(self, start):
        q=[]

        q.append(start)
        self.nodes[start][0]=True
        
        while q:
            w=q.pop(0)
            print(w)
            if self.nodes[w][1]!=None:
                for z in self.nodes[w][1]:
                    if self.nodes[z][0]==False:
                        self.nodes[z][0]=True
                        q.append(z)

    def DFS(self, start):
        s=[]

        s.append(start)
        self.nodes[start][0]=True
        
        while s:
            w=s.pop()
            print(w)
            if self.nodes[w][1]!=None:
                for z in self.nodes[w][1]:
                    if self.nodes[z][0]==False:
                        self.nodes[z][0]=True
                        s.append(z)

    def DFSRec(self, start):
        print(start)
        if self.nodes[start][1]!=None:
            for z in self.nodes[start][1]:
                if self.nodes[z][0]==False:
                    Graph.DFSRec(self, z)

nodeDict={"a": [False, ["b", "c"]],
          "b": [False, ["d", "e"]],
          "c": [False, ["f", "g"]],
          "d": [False, None],
          "e": [False, None],
          "f": [False, None],
          "g": [False, None],}


test=Graph(nodeDict)
test.DFSRec("a")




            
        
    
