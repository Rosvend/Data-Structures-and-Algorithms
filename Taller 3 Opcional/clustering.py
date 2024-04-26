import heapq as hq
import matplotlib.pyplot as plt
import csv
from math import sqrt
import time
from random import uniform
from collections import Counter
import numpy as np

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
        self.uf = UnionFind(len(data))
    
    def distance(self,x,y):
        return sqrt(sum((x-y)**2 for x, y in zip(x,y)))
    
    def cluster(self,dmax):
        start_time = time.time()
        distances = []
        
        for i in range(len(self.data)):
            for j in range(i+1,len(self.data)):
                dist = self.distance(self.data[i],self.data[j])
                hq.heappush(distances,(dist,(i,j)))
        
        clusters = []
        while distances and distances [0][0] <dmax:
            _, (i,j) = hq.heappop(distances)
            self.uf.union(i,j)
        
        clusters = set(self.uf.find(i) for i in range(len(self.data)))

        end_time = time.time()
        total_time = end_time - start_time
        print (f'Total time was {total_time:.6f} seconds')
        return len(clusters)
    
    def classify(self,p,k):
        """Classify new points with nearest k neighbors

        Args:
            p (int): 2d point
            k (int): number of neighbor
        """

        distances = [(self.distance(p,point),i) for i, point in enumerate(self.data)]
        kneighbors = sorted(distances)[:k]
        clusters = [self.uf.find(i) for _, i in kneighbors]
        most_common_cluster = Counter(clusters).most_common(1)[0][0]

        return most_common_cluster


    def graficarClusteres(cluster_ids, data):
        unique_clusters = list(set(cluster_ids))
        n_colors = len(unique_clusters)
    
        colors = plt.cm.get_cmap('viridis', n_colors)
    
        cluster_color_map = dict(zip(unique_clusters, range(n_colors)))
    
        for idx, point in enumerate(data):
            cluster_id = cluster_ids[idx]
            color_idx = cluster_color_map[cluster_id]
            plt.scatter(point[0], point[1], color=colors(color_idx))
    
        handles, labels = plt.gca().get_legend_handles_labels()
        unique = [(h, l) for i, (h, l) in enumerate(zip(handles, labels)) if l not in labels[:i]]
        plt.legend(*zip(*unique))
    
        plt.title("Visualization of Clusters")
        plt.xlabel("X Coordinate")
        plt.ylabel("Y Coordinate")
        plt.show()

    def randomTest(cl, k=5):
        random_points = [(uniform(-2, 2), uniform(-2, 2)) for _ in range(10)]
        print("Random Points:", random_points)  
    
        for point in random_points:
            classifications = cl.classify(point, k)
        
            distances = sorted([(cl.distance(point, data_point), i) for i, data_point in enumerate(cl.data)])
            kneighbors = [cl.uf.find(i) for _, i in distances[:k]]
            print(f"K-nearest neighbors for point ({point[0]:.3f}, {point[1]:.3f}): {kneighbors}")
            print(f"Point ({point[0]:.3f}, {point[1]:.3f}) is classified into cluster {classifications}")
            print()

class Taller3Opcional:

    @staticmethod
    def leer_puntos(filename):
        points = []
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for line_number, row in enumerate(reader, 1):
                try:
                    if len(row) == 2:
                        x, y = map(float, row)
                        points.append((x, y))
                        print(f"Line {line_number}: Read point ({x}, {y})")
                    else:
                        print(f"Line {line_number}: Incorrect number of columns")
                except ValueError as e:
                    print(f"Line {line_number}: Error reading row {row} - {e}")
        return points

    @staticmethod
    def main(filename):
        dmax = float(input('Please enter your maximum distance threshold: '))
        points = Taller3Opcional.leer_puntos(filename)
        cl = clustering(points)
        num_clusters = cl.cluster(dmax)
        print(f'Number of clusters: {num_clusters} clusters')

        cluster_ids = [cl.uf.find(i) for i in range(len(points))]
        clustering.graficarClusteres(cluster_ids, points)

        clustering.randomTest(cl)


Taller3Opcional.main(r"C:\Users\royda\OneDrive\Documentos\Universidad\3. Tercer semestre\Estructuras de datos y algoritmos\Talleres\Taller 3 Opcional\datapoints-1000.csv")

