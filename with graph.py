#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 13:00:32 2018

@author: shubhadaaute
"""

import random

import matplotlib.pyplot as plt

Dice = [1,2,3,4,5,6]
#This has all the values from output of dice

prob_sum = [[2,1/36],[3,2/36],[4,3/36],[5,4/36],[6,5/36],[7,6/36],[8,5/36],[9,4/36],[10,3/36],[11,2/36],[12,1/36]]
#This is a dictionary assigns probability for each sum that we get from 2 dice

money_dist = []
for i in prob_sum:
    money_dist.append(0.11-i[1])
#We have probability distribution for dice sum. Now this gives inverted form of sum distribution. So, this distribution of money will be followed for each sum in output.    

money_given = [i * 1500 for i in money_dist ]
#We just multiply with some number so that we get exact amout that gambler will get or give following the money distribution.
money_dict = {}
for i in range(2,13):
    money_dict[i] = money_given[i-2]

#s = random.choice(Dice) + random.choice(Dice)
#This gives sum of numbers on dice randomly.
#gm = []
#Money that gamber gets in each iteration
gambler_profit = []
# This is basically addition of all money that gamber gets upto i th iteration.
owner_profit = []

D = 0
# Dummy variable which will everytime give cummulative profit of gambler
Do = 0
#Dummy variable for owner



xAxis = []
for i in range(100):
    xAxis.append(i+1)
    s = random.choice(Dice) + random.choice(Dice)
    for keys in money_dict:
        if keys == s:
            gm = money_dict[s]
            D = D + gm
            gambler_profit.append(D)
            
            Do = Do - gm
            owner_profit.append(Do)
            
            
print(gambler_profit)
print(owner_profit)

plt.xlabel("Number of transactions")
plt.ylabel("Rupees")
plt.plot(xAxis, gambler_profit, 'b', label = "Gambler's net profit")
plt.plot(xAxis, owner_profit, 'r', label = "Owner's net profit")
plt.legend()
plt.show()