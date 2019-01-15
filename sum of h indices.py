#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 13:27:50 2019

@author: shubhadaaute
"""

import networkx as nx
import matplotlib.pyplot as plt
import random
L={}
G=nx.gnp_random_graph(10,0.4)
nx.draw(G, with_labels=True)
plt.show()
for i in range(0,10):
    k=random.randint(1,G.degree(i)+2)
    L[i]=k
    
print(L)   
N={}

for i in range(0,10):
    N[i]=(list(G.neighbors(i)))
print(N)
M={}
for i in N:
    M[i]=[]
    for j in N[i]:
        M[i].append(L[j])
    
print(M)
H={}

for i in range(0,10):
    M[i].sort()
    M[i].reverse()
    for j in range(len(M[i])):
        if j < M[i][j]:
            j=j+1
            if j==len(M[i]):
                H[i]=j
                break
        else:
            H[i]=j
            break
    
print(H)    
sum1=0
for i in range(0,10):
    sum1=sum1+H[i]
print(sum1)

L2=H

M2={}
for i in N:
    M2[i]=[]
    for j in N[i]:
        M2[i].append(L2[j])
    
print(M2)
H2={}

for i in range(0,10):
    M2[i].sort()
    M2[i].reverse()
    for j in range(len(M2[i])):
        if j < M2[i][j]:
            j=j+1
            if j==len(M2[i]):
                H2[i]=j
                break
        else:
            H2[i]=j
            break
    
print(H2)    
sum2=0
for i in range(0,10):
    sum2=sum2+H2[i]
print(sum2)












'''
N1=[]

for i in range(list(G.neighbors(3))):
    N1.append(L[i])
print(N1)
for i in range(len(L)):
    if i<L[i]:
          i=i+1
          if i==len(L):
            print(i)
            break
    else:
        print(i)
        break'''
            