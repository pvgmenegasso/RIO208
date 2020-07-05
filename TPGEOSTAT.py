# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

import matplotlib.pyplot as mp

import random as rd

import seaborn as sns

GAMMA = 2.5
SIGMA =  2
LAMBDA = 50
SIGA = 1
LAMBDA2 = 500

## Classes

class Point:
    
    def __init__(self, coord, value):
        self.x = coord[0]
        self.y = coord[1]
        self.coord = [coord[0],coord[1]]
        self.value = value
        
        
        


print(1/(2*np.sqrt(LAMBDA)))

## Fonctions
def distance(coorda, coordb):
    return np.sqrt(np.power(coorda[0] - coordb[0], 2) + np.power(coorda[1] - coordb[1], 2))

def question1():
    area = np.power(1, 2)
    
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
        x = rd.uniform(0, 1)
        y = rd.uniform(0, 1)
        arrx.append(x)
        arry.append(y)
    return arrx, arry, N

def question4():
    area = np.power(1, 2)
    
    exp = (-1/(LAMBDA2*area))*np.log(rd.random()%1)
    
    curr = 1
    
    sum = exp
    
    while sum <= 1:
        x = rd.random()%1
        exp = (-1/(LAMBDA2*area))*np.log(rd.random()%1)
        curr += 1
        sum = sum+exp
        
    N = curr - 1
    arrx = []
    arry = []
    
    for i in range(N):
        x = rd.uniform(0, 1)
        y = rd.uniform(0, 1)
        arrx.append(x)
        arry.append(y)
    return arrx, arry, N


def puissancei(utilisateur, station):
    dist = distance(utilisateur, station)
    if (dist <= 0.005):
        dist = 0.005
    puiss = rd.uniform(0, 1)
    fading = -(1/SIGA)*np.log(rd.uniform(0,1))
    shadow = np.power(10, (SIGMA*rd.random()/10))

    return (puiss/(np.power(dist, GAMMA)))*fading*shadow
    



def sir(arrx, arry, utilisateur, N):
    ## first we have to see which station is the closest to x y
    stationserveuse = -1
    distmin = 100000
    for i in range(N):  
        dist = distance([arrx[i],arry[i]], utilisateur)
        if (dist < distmin):
            distmin = dist
            stationserveuse = i
            
    puisserveuse = puissancei(utilisateur, [arrx[stationserveuse], arry[stationserveuse]])
    
    total = 0
            
    ## now to calculate the divisor
    
    for i in range(N):
        if(i != stationserveuse):
            total = total + puissancei(utilisateur, [arrx[i], arry[i]]) 
            
    if (total - puisserveuse == 0):
        return 0
    
        
    value = (puisserveuse/(total - puisserveuse))
    
    if (value < 0):
        value = - value
        
    
    
    
    return 10*np.log10(value)


def sir2(arrx, arry, utilisateur, N):
    ## first we have to see which station is the more powerfull
    stationserveuse = -1
    puissmax = 0
    for i in range(N):  
        puiss = puissancei(utilisateur, [arrx[i], arry[i]])
        if (puiss > puissmax):
            puissmax = puiss
            stationserveuse = i
            
    puisserveuse = puissancei(utilisateur, [arrx[stationserveuse], arry[stationserveuse]])
    
    total = 0
            
    ## now to calculate the divisor
    
    for i in range(N):
        if(i != stationserveuse):
            total = total + puissancei(utilisateur, [arrx[i], arry[i]]) 
            
    if (total - puisserveuse == 0):
        return 0
    
        
    value = (puisserveuse/(total - puisserveuse))
    
    if (value < 0):
        value = - value
        
    
    
    
    return 10*np.log10(value)
        
        

## Question 1


#Calculer poisson
arrx, arry, N = question1()

mp.plot(arrx, arry, "go", label = "stations")
mp.title("question 1")
mp.legend()
mp.show()

## Question 1.2


dist = []
iterations = 10000
lambd = 50
sum = 0
for i in range(iterations):
    N = np.random.poisson(lambd)
    sum += N
    dist.append(N)

    
moyenne = sum/iterations
print("the mean is", moyenne)
mp.title("question 1.2")
mp.hist(dist, label = "quantité de distribuitions avec chaque quantité de valeurs", ec = "black")
mp.legend()
mp.show()

## question 1.3
## on revien a la premiere question:
    
arrx, arry, N = question1()
    
## maintenant on calcule la distance moyenne entre les points

dists = []
dist = 10
for i in range(N):
    coorda = [arrx[i], arry[i]]
    dists.append(0)
    for j in range(N):
        if i != j: ## ne pas caluler la distance entre un point et soi meme
            coordb = [arrx[j], arry[j]]
            newdist = distance(coorda, coordb)
            if newdist < dist:
                dist = newdist
                dists[i] = dist
            
    dist = 10
    

                
print("les distances sont:", dists)

mp.title("question 1.3")
mp.hist(dists, ec = "black", label="distribuition de chaque distance")
mp.legend()
mp.show()

print("moyenne des distances: ", np.mean(dists))

## question  3
        
        
## Question 3.5

N = 100

arrxd = []
arryd = []


for i in range(101):
    
    for j in range(101):

        arrxd.append(i/100)
        arryd.append(j/100)


mp.scatter(arrxd, arryd, s=0.5)
mp.show()

## Question 3.6

## Regenerer la distribuition:
    
arrx, arry, N = question1()

ma = mp.plot(arrx, arry, "go", label = "stations")
mp.show()

## populer matriz des SIR:
    
sirx = []
siry = []
arr = np.empty(shape=[101, 101])
j = 0

for i in range(101):
    

        
    for j in range(101):

        arr[i][j] = (sir(arrx, arry, [i/100, j/100], N))

        

print(sirx)
print(siry)

multiplyer = lambda x: x*100

arrx100 = [x * 100 for x in arrx]
arry100 = [x * 100 for x in arry]

ax = sns.heatmap(arr, cmap="YlGnBu_r", alpha = 0.8)
ma = mp.plot(arrx100, arry100, "go", label = "stations")
ax.invert_yaxis()
mp.show(ax, ma)


## Question 3.7 critere puissance


j = 0
for i in range(101):
    

        
    for j in range(101):

        arr[i][j] = (sir2(arrx, arry, [i/100, j/100], N))

ax = sns.heatmap(arr, cmap="YlGnBu_r", alpha = 0.8)
mp.plot(arrx100, arry100, "go", label = "stations")
ax.invert_yaxis()
mp.show() 


## Question 4


#Calculer poisson
arrx2, arry2, N2 = question4()

mp.plot(arrx2, arry2, "go", label = "utilisateurs")
mp.title("question 4")
mp.legend()
mp.show()

## Question 4.9

##utilisateurparcelule = np.empty(shape = [N]) 

utilisateurparcelule = [0]*N

# on va trier parmi 100 simulations
celule = -2
for i in range(100):
   
    for utilisateur in range(len(arrx2)):

        distancemin = 10000
        
        for station in range(len(arrx)):
   
            newdistance = distance([arrx2[utilisateur], arry2[utilisateur]], [arrx[station], arry[station]]) 
            
            if newdistance < distancemin:
                
                distancemin = newdistance
                celule = station
                
        utilisateurparcelule[celule] = utilisateurparcelule[celule]+1
        
        
for i in range(len(utilisateurparcelule)):
    
    utilisateurparcelule[i] = utilisateurparcelule[i]/100
        
mp.title("question 4.9")
mp.hist(utilisateurparcelule, ec = "black", label="quantité de utilisateurs pour chaque celule (100 tris)")
mp.legend()
mp.show()   

   

print("moyenne:")
print(np.mean(utilisateurparcelule))

# 4.11

arrsir = [0]*len(arrx2)

for j in range(100):

    for i in range(len(arrx2)):
        
            
            arrsir[i] = arrsir[i]+sir(arrx, arry, [arrx2[i], arry2[i]], N)
        

mp.title("question 4.11")
mp.hist(arrsir, ec= "black", label = "histogramme SIR utilisateurs (100 simulations)")
mp.legend()
mp.show() 

sirx = []
siry = []
arr = np.empty(shape=[101, 101])

sirs = [0]*101*101
countsirs = 0

for z in range(100):

    for i in range(101):
        
    
            
        for j in range(101):
    
            sirs[countsirs]  += (sir(arrx, arry, [i/100, j/100], N))
            countsirs += 1
            
    countsirs = 0
    
            



mp.title("question 4.11/2")
mp.hist(sirs, ec = "black", label = "histogramme SIR pixels (100 simulations)")
mp.show()
             
    
    


