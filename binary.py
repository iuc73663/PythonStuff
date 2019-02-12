# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 16:11:07 2019

@author: Administrator
"""

import math

#used for "rule"
def defineKey(rule):
    return ('{0:08b}'.format(rule))

#used for 7-0
def binaryRule(rule):
    return ('{0:03b}'.format(rule))

#maps rule in base 2 to "keys"
def ruleMapping(rule):
    binRule = defineKey(rule)
    mapList = {}
    j = 0
    for i in reversed(range(8)):
        mapList[binaryRule(i)] =  binRule[j:j+1]
        j +=1
    return mapList

#prints matrix
def printGrid(grid, r,c):
    b = ""
    for i in range(r):
        for j in range(c): 
            b += str(grid[i][j])
            b += " "
            if(j == (c - 1)):
                b += "\n"
    print(b)


#hard coded rule 
ruleMap = ruleMapping(30)

#hard coded steps (rows) 
h = 2 
#columns
w = 3
#create grid based on above
ruleGrid = [[0 for x in range(w)] for y in range(h)]
#step 1
ruleGrid[0][(math.floor(w/2))] = 1

#preview
printGrid(ruleGrid,h,w)


