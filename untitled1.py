#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 16:36:59 2019

@author: shubhadaaute
"""


'''L=[3,9,1,4,2,7,5,6,4,6,7]
L.sort()
L.reverse()
for i in range(len(L)):
    if L[i] < (i+1):
        print(i)
    else:
        i=i+1'''
     
#This prints every value.
        

L=[3,9,1,4,2,7,5,6,4,6,7]
L.sort()
L.reverse()
'''for i in range(len(L)):
    if i<L[i]:
        i=i+1
    else:
        print(i)
        break'''
    
#This code will give H indices.  
'''for i in range(len(L)):
    if i < L[i]:
            i=i+1
    else:
        
        print(i)
        break'''
            
def H-operator(L):
    for i in range(len(L)):
    if i<L[i]:
          i=i+1
          if i==len(L):
            print(i)
            break
    else:
        print(i)
        break
return(i)