#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 17:23:39 2020

@author: pvgmenegasso
"""
import numpy as np
import random as rd
import matplotlib.pyplot as mp


LAMBDA = 0.01
RAYON = 320
C = 162
OMEGA = 180
SNRMIN = 0.1    
K = np.power(10, 6)
GAMMA = 2.8


def q2(arrx):
    
    indexes = actifs(arrx)

    actifsx = []
    actifsy = []

    for i in range(len(indexes)):
        actifsx.append(arrx[indexes[i]])
        actifsy.append(arry[indexes[i]])
        
    return actifsx, actifsy

def distance(coorda, coordb):
    return np.sqrt(np.power(coorda[0] - coordb[0], 2) + np.power(coorda[1] - coordb[1], 2))

def qmax():
    valeur = C / (OMEGA*np.log2(1+SNRMIN))
    return valeur

def qx(coord):
    valeur = C / (OMEGA * np.log2(1 + (K / (np.power(distance([coord[0], coord[1]], [RAYON, RAYON]), GAMMA)))))
    return valeur


def question1():
    area = np.power(RAYON*2, 2)
    
    exp = (-1/(LAMBDA*area))*np.log(rd.random()%1)
    
    curr = 1
    
    sum = exp
    
    while sum <= 1:
        x = rd.random()%1
        exp = (-1/(LAMBDA*area))*np.log(rd.random()%1)
        curr += 1
        sum = sum+exp
        
    N = curr - 1
    arrx = []
    arry = []
    
    for i in range(N):
        x = rd.uniform(0, RAYON*2)
        y = rd.uniform(0, RAYON*2)
        ## verifie si le point est dans le disque
        dist = distance([x, y], [RAYON,RAYON])
        if dist <= RAYON:
            
            arrx.append(x)
            arry.append(y)
            
            
    return arrx, arry, N

def actifs(arrx):
    indexes = []
    for utilisateur in range(len(arrx)):
        rand = rd.randint(1, 100)

        
        if rand == 50:      ## probabilité de 1%
            indexes.append(utilisateur)

    return indexes
## Question 1

arrx, arry, N = question1()

mp.plot(arrx, arry, "go", label = "utilisateurs")
mp.title("question 1")
mp.legend()
mp.show()

## Question 2

actifsx, actifsy = q2(arrx)
 
mp.plot(actifsx, actifsy, "go", label = "utilisateurs actifs")
mp.title("question 2")
mp.legend()
mp.show()

## Question 3 

print("qmax = ",np.round_(qmax(), 0))


## Question 4


## il faut verifier chaque S


outages = [0]*20
index = 0

for s in range(160, 180):
    
    

    ## il faut faire 10000 simulations
    
    for simulation in range(10000):
    
        actifsx, actifsy = q2(arrx)
        
        f = 0
        
        for user in range(len(actifsx)):
            
            f = f + qx([actifsx[user], actifsy[user]])
            
        if f >= s:
            
            outages[index] = outages[index] + 1
            
        
    index = index + 1
    
    
    
print(outages)
    
            
        
        







