import heapq as hq 
import csv
from math import sqrt
import time
from random import randint
from collections import Counter

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
    
    def cluster(self,D):
        start_time = time.time()
        distances = []
        
        for i in range(len(self.data)):
            for j in range(i+1,len(self.data)):
                dist = self.distance(self.data[i],self.data[j])
                hq.heappush(distances,(dist,(i,j)))
        
        clusters = []
        while distances and distances [0][0] <D:
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
            p (int): coordinate X of point to classify
            k (int): coordinate Y of point to classify
        """

        distances = [(self.distance(p,point),i) for i, point in enumerate(self.data)]
        kneighbors = sorted(distances)[:k]
        clusters = [self.uf.find(i) for _, i in kneighbors]
        most_common_cluster = Counter(clusters).most_common(1)[0][0]

        return most_common_cluster


    def randomtest(self):
        points = [(randint(0,100), randint(0,100)) for _ in range(10)]
        classifications = [self.classify(point,k) for point in points]
        return classifications
    

    


def leer_puntos(filename):


    """Lee el archivo CSV"""
    points = []
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar el encabezado
        for row in reader:
            x,y = map(float,row[0].split(','))
            points.append((x,y))
    return points


def main(filename):

        D = int(input('Please enter your maximum distance threshold:  '))
        points = leer_puntos(filename)
        cl = clustering(points)
        num_clusters = cl.cluster(D)
        print(f'Number of clusters: {num_clusters} clusters')

        classifications = cl.randomtest()
        print(f'Classifications of 10 random points: {classifications}')


file_path = r"C:\Users\royda\OneDrive\Documentos\Universidad\3. Tercer semestre\Estructuras de datos y algoritmos\Talleres\Taller 3 Opcional\datapoints-k=2-n=200.csv"
main(file_path)