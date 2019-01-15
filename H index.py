#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 22:22:52 2019

@author: shubhadaaute
"""


import networkx as nx
import matplotlib.pyplot as plt
import random
L={}
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

L3=H2

M3={}
for i in N:
    M3[i]=[]
    for j in N[i]:
        M3[i].append(L3[j])

print(M3)
H3={}

for i in range(0,10):
    M3[i].sort()
    M3[i].reverse()
    for j in range(len(M3[i])):
        if j < M3[i][j]:
            j=j+1
            if j==len(M3[i]):
                H3[i]=j
                break
        else:
            H3[i]=j
            break

print(H3)    
sum3=0
for i in range(0,10):
    sum3=sum3+H3[i]
print(sum3)


L4=H3

M4={}
for i in N:
    M4[i]=[]
    for j in N[i]:
        M4[i].append(L4[j])

print(M4)
H4={}

for i in range(0,10):
    M4[i].sort()
    M4[i].reverse()
    for j in range(len(M4[i])):
        if j < M4[i][j]:
            j=j+1
            if j==len(M4[i]):
                H4[i]=j
                break
        else:
            H4[i]=j
            break

print(H4)    
sum4=0
for i in range(0,10):
    sum4=sum4+H4[i]
print(sum4)