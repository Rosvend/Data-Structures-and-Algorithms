#Create a min priority queue
class min_priority_queue:
    def __init__(self):
        self.queue = []
    
    def insert(self, value):
        self.queue.append(value)
        self.queue.sort()
    
    def extract_min(self):
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def min(self):
        return self.queue[0]


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