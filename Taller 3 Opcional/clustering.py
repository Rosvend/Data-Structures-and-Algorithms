import heapq as hq 

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        
        if x_root == y_root:
            return False
        
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1
        
        return True


class clustering:
    def __init__(self, data):
        self.data = data
        self.clusters = []
        self.centroids = []
    
    def cluster(self, k):
        self.centroids = self.data.sample(n=k)
        self.clusters = [self.centroids.index.tolist()]
        
        for i in range(k):
            self.clusters.append([])
        
        for index, row in self.data.iterrows():
            min_dist = float('inf')
            cluster = -1
            for i in range(k):
                dist = self.euclidean_distance(row, self.centroids.loc[i])
                if dist < min_dist:
                    min_dist = dist
                    cluster = i
            self.clusters[cluster+1].append(index)
        
        for i in range(k):
            self.centroids.loc[i] = self.data.loc[self.clusters[i+1]].mean()
        
        return self.clusters, self.centroids