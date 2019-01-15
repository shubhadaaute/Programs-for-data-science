#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 12:42:22 2019

@author: shubhadaaute
"""

import networkx as nx
import matplotlib.pyplot as plt
import random
L(1)={}
G=nx.gnp_random_graph(10,0.7)
nx.draw(G, with_labels=True)
plt.show()
for i in range(0,10):
    k=random.randint(1,G.degree(i)+2)
    L[i]=k
print(L)   
N={}

for i in range(0,10):
    N[i]=(list(G.neighbors(i)))
#print(N)
for K in range(1,10):
    M(K)={}
    for i in N:
        M(K)[i]=[]
        for j in N[i]:
            M(K)[i].append(L(K)[j])
    
   #print(M(K))
    H(K)={}

    for i in range(0,10):
        M(K)[i].sort()
        M(K)[i].reverse()
        for j in range(len(M(K)[i])):
            if j < M(K)[i][j]:
                j=j+1
                if j==len(M(K)[i]):
                    H(K)[i]=j
                    break
            else:
                H(K)[i]=j
                break
    
   #print(H(K))    
    sum(K)=0
    for i in range(0,n):
        um(K)=sum(K)+H(K)[i]
    print(sum(K))
    L(K+1)=H(K)  