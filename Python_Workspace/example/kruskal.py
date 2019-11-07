class Graph(object):
    def __init__(self, maps):
        self.maps = maps
        self.nodenum = self.get_nodenum()
        self.edgenum = self.get_edgenum()
 
    def get_nodenum(self):   #求图的顶点数
        return len(self.maps)
 
    def get_edgenum(self):  #求图的边数
        count = 0
        for i in range(self.nodenum):
            for j in range(i):
                if self.maps[i][j] > 0 and self.maps[i][j] < 9999:
                    count += 1
        return count
 
    def kruskal(self):
        res = []
        if self.nodenum <= 0 or self.edgenum < self.nodenum-1:  #边不足或点不足，则不做操作
            return res
        edge_list = []
        for i in range(self.nodenum):
            for j in range(i,self.nodenum):
                if self.maps[i][j] < 9999:
                    edge_list.append([i, j, self.maps[i][j]])#按[begin, end, weight]形式加入
        edge_list.sort(key=lambda a:a[2])    #以weight将边集排序存放
        
        group = [[i] for i in range(self.nodenum)]
        for edge in edge_list:
            for i in range(len(group)):
                if edge[0] in group[i]:
                    m = i
                if edge[1] in group[i]:
                    n = i
            if m != n:
                res.append(edge)
                group[m] = group[m] + group[n]
                group[n] = []
        return res
    
max_value = 9999
row0 = [0,8,max_value,7,9]   
row1 = [8,0,2,max_value,1]
row2 = [max_value,2,0,3,max_value]
row3 = [7,max_value,3,0,6]
row4 = [9,1,max_value,6,0]
#row5 = [5,max_value,max_value,10,4,0]
maps = [row0,row1,row2,row3,row4]  #定义邻接矩阵
graph = Graph(maps)  #实例化Graph类
print('邻接矩阵为\n%s' %graph.maps)
print('节点数据为%d，边数为%d\n'%(graph.nodenum, graph.edgenum))
print('------最小生成树kruskal算法------')
print(graph.kruskal())
