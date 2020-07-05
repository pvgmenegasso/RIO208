#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 20:54:40 2020

@author: pvgmenegasso
"""


import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as mp
import matplotlib.patches as patches


df1 = pd.read_csv("~/Documents/TPsRIO/Fichiers CSV/o_gsm.csv")

print(df1)


arrx = df1['Longitude']
arry = df1['Latitude']

## definition du rectangle:
    
##definition de la talle
x = 144000
y = 7000

xs =[-7500, -7500+x, -7500, -7500+x]
ys =[-4000, -4000, -4000+y, -4000+y]



rect = patches.Rectangle((-x/2, -y/2), x, y)


mp.plot(arrx, arry, "go", label = "stations gsm orange")
ax = mp.gca()
ax.add_patch(rect)
mp.legend()
mp.show()