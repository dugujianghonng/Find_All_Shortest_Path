#该代码用于寻找图中对于给定起点和终点的所有最短路径
class node:
    """
    结点类
    """
    def __init__(self,val,path,dis):
        """
        结点类的初始化
        :param val:  结点序号
        :param path: 存储该结点到起点的当前最短路径
        :param dis:  存储该结点到起点的当前最短距离
        """
        self.val = val
        self.path = path
        self.dis = dis
# Press the green button in the gutter to run the script.
def Find_All_Shortest_Path(graph, start, end):
    """
    :param            graph:  所输入图结点之间的距离矩阵
    :param            start:  起点
    :param              end:  终点
    :return: shortest_paths:  所有的最短路径集合
    """
    paths = []
    n = len(graph)                           # 结点个数
    distance = [float('inf')] * n            # 存储每个结点到起点的当前最短距离
    queue = []                               # 存储结点到起点的当前局部路径信息
    queue.append(node(start, [start], 0))
    min_dis          = float('inf')
    distance[start] = 0
    paths           = []
    shortest_paths  = []
    while (queue):
        s = queue.pop(0)
        if (s.val == end and s.dis <=min_dis):
            min_dis = s.dis
            paths.append(s)
        if (s.dis >=min_dis):                #剪枝
            pass
        else:
            for i in range(n):
                if (graph[s.val][i] != float('inf') and distance[i] >= graph[s.val][i]):
                    queue.append(node(i, s.path + [i], s.dis + graph[s.val][i]))
                    distance[i] = s.dis + graph[s.val][i]
    for p in paths:
        if p.dis == min_dis:
            shortest_paths.append(p)
    return shortest_paths
if __name__ == '__main__':
    graph = [
        [float('inf'),            5,            4, float('inf'), float('inf'), float('inf'), float('inf')],
        [           5, float('inf'),            6, float('inf'), float('inf'),            4, float('inf')],
        [           4,            6, float('inf'),            7, float('inf'),            6, float('inf')],
        [float('inf'), float('inf'),            7, float('inf'),            4, float('inf'),            3],
        [float('inf'), float('inf'), float('inf'),            4, float('inf'),            3,            4],
        [float('inf'),            4,            6, float('inf'),            3, float('inf'),            5],
        [float('inf'), float('inf'), float('inf'),            3,            4,            5, float('inf')]]
    start = 0
    end   = 6
    shortest_paths = Find_All_Shortest_Path(graph, start, end)
    for p in shortest_paths:
        print(p.path, p.dis)