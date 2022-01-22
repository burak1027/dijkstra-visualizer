import timeit

import numpy as np
import networkx
import matplotlib.pyplot as plt
import time
import tkinter as tk
import math
import sys
nodelist=[]

def createNode(N):
    global nodelist
    arr = np.zeros((N,N),dtype=int)
    if(N%2==1):
        arr[N - 2][N-1] = N*2-3
        arr[N-1 ][N - 2] = N*2-3
        arr[N-3][N - 1] = N*2-3
        arr[N - 1][N-3] = N*2-3
        N=N-1

    arr[N - 2][N - 1] = N*2-3
    arr[N - 1][N - 2] = N*2-3
    for i in range(N-2):
        a=2+((i+1)%2)
        temp=[]
        for j in range(i+1,i+a+1):
            arr[i][j]=i+j
            arr[j][i]=i+j
            temp.append(j)
    return arr
def graph(list2):
    arr=[]
    for i in list2:
        arr2=[]
        counter=0
        for a in i:
            if a!=0:
               arr2.append(counter)
            counter+=1

        arr.append(arr2)

    return arr

class Heap():
    def __init__(self):
        self.array = []
        self.size = 0
        self.pos = []

    def newMinHeapNode(self, v, dist):
        minHeapNode = [v, dist]
        return minHeapNode

    def swapMinHeapNode(self, a, b):
        t = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t

    def minHeapify(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < self.size and self.array[left][1] < self.array[smallest][1]:
            smallest = left
        if right < self.size and self.array[right][1] < self.array[smallest][1]:
            smallest = right
        if smallest != idx:
            self.pos[self.array[smallest][0]]= idx
            self.pos[self.array[idx][0]] =smallest

            self.swapMinHeapNode(smallest, idx)

            self.minHeapify(smallest)

    def extractMin(self):

        if self.isEmpty() == True:
            return

        root = self.array[0]
        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
        self.size -= 1
        self.minHeapify(0)

        return root

    def isEmpty(self):
        return True if self.size == 0 else False

    def isInMinHeap(self, v):
        if self.pos[v] < self.size:
            return True
        return False

    def decreaseKey(self, v, dist):
        i = self.pos[v]
        self.array[i][1] = dist
        while i > 0 and self.array[i][1] < self.array[int((i - 1) / 2)][1]:

            self.pos[self.array[i][0]] = int((i - 1) / 2)
            self.pos[self.array[int((i - 1) / 2)][0]] = i
            self.swapMinHeapNode(i, int((i - 1) / 2))
            i = int((i - 1) / 2);


def dijkstra(start,nodes,accesibleNodes):
    prev = []
    numberOfVertices=len(nodes)
    distances=[]
    minHeap = Heap()
    for i in range(numberOfVertices):
        distances.append(999999999)
        minHeap.array.append(minHeap.newMinHeapNode(i,distances[i]))
        minHeap.pos.append(i)
        prev.append(0)

    minHeap.pos[start]=start
    distances[start]=0
    minHeap.decreaseKey(start,distances[start])
    minHeap.size=numberOfVertices
    while minHeap.isEmpty() == False:
        extractedNode=minHeap.extractMin()
        a=extractedNode[0]
        # print(a)
        for i in accesibleNodes[a]:
                if minHeap.isInMinHeap(i) and nodes[a][i] + distances[a] < distances[i]:
                    distances[i]=nodes[a][i] + distances[a]
                    prev[i]=a
                    minHeap.decreaseKey(i,distances[i])
                    # print(distances)
    # print(prev)
    return distances,prev


def visualize(accesibleNodes,path):
    G = networkx.Graph()
    red_nodes=[]
    for i in range(len(path)-1,0,-1):
        red_nodes.append((path[i-1],path[i]))
    for i in range(len(accesibleNodes)):
        G.add_node(i,pos=(i-(i%2),(-(i%2))+0.2))
        count=0
    for i in accesibleNodes:
        for j in i:
            G.add_edge(count,j)
        count+=1
    pos=networkx.get_node_attributes(G,'pos')
    networkx.draw(G,pos,with_labels=1)
    networkx.draw_networkx_edges(G,pos,edgelist=red_nodes,edge_color='r')
    plt.ylim(-2, 2)
    plt.show()


def dijks(N, S,D):
    nodes = createNode(N)
    accesibleNodes = graph(nodes)
    start_time = time.time()
    temp =dijkstra(S, nodes, accesibleNodes)
    list = temp[1]
    j = D
    list2 = []
    list2.append(j)
    while list[j] != S:
        j = list[j]
        list2.append(j)
    list2.append(S)
    end_time = time.time()
    rtn=end_time-start_time
    distance=temp[0]
    cost=distance[D]
    return list2,rtn,cost

def draw(N,S,D):
    nodes = createNode(N)
    accesibleNodes = graph(nodes)
    list2 = dijks(N, S, D)[0]
    visualize(accesibleNodes, list2)
    return dijks(N, S, D)[1]

def Graph(list):
    times=[]
    theo=[]
    for i in list:
        a=E(graph(createNode(i)))*math.log(10,i)/100000
        theo.append(a)
        times.append(dijks(i,0,i-1)[1])
    plt.plot(list,times,marker='o')
    plt.plot(list,theo,marker='o')
    plt.ylabel("Running Time")
    plt.xlabel("Number of Nodes")
    plt.xticks()
    plt.legend(['Actual running time','Theoretical running time'])

    plt.show()

def E(list):
    count = 0
    for i in list:
        for j in i:
            count+=1
    return count

if __name__ == '__main__':
    Graph([10,50,200,500,1000,2000])

    a=dijks(10,0,6)
    a[0].reverse()
    print("path = ",a[0])
    # print("running time = ",a[1]," seconds")
    print("cost =",a[2])

    # print("-----")
    # print(list2)
























