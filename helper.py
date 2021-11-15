# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 15:44:57 2021

@author: Rishi2
"""

import json

length_desc = {
    
    "ft": "feet",
    "in": "inches",
    "cm": "centimeters",
    "m": "meters",
    "km": "kilometers"
    }

length_units = length_desc.keys()

graph = {}

for un in length_units:
    graph[un] = {}
    
graph['ft']['in'] = 12
graph['in']['cm'] = 2.54
graph['m']['cm'] = 100
graph['km']['m'] = 1000

# make the edges bidirectional
for unit in graph:
    for other_unit in graph[unit]:
        if unit not in graph[other_unit]:
            graph[other_unit][unit] = 1/graph[unit][other_unit]
            
# convert any two units
def convert(unit_1, unit_2, length_units, graph):
    units = [unit_1]
    visited = {}
    parent = {}
    for unit in length_units:
        visited[unit] = False
        parent[unit] = None
    while len(units) != 0:
        curr = units[0]; units = units[1:]
        neighbors = graph[curr].keys()
        for other_u in neighbors:
            if not visited[other_u]:
                units.append(other_u)
                parent[other_u] = curr
                visited[other_u] = True
    prevPar = unit_2
    currPar = parent[prevPar]
    invRet = 1
    while currPar != unit_1:
        invRet *= graph[prevPar][currPar]
        prevPar = currPar
        currPar = parent[currPar]
    invRet *= graph[prevPar][unit_1]
    return 1/invRet

other_gr = {}

for un in length_units:
    other_gr[un] = {}
    for other_un in length_units:
        if un == other_un:
            other_gr[un][un] = 1
        else:
            conversion = convert(un, other_un, length_units, graph)
            other_gr[un][other_un] = round(conversion, 3)
print(other_gr)

f = open("len_conv.json", "w")
json.dump(other_gr, f)
f.close()

f = open("len_desc.json", "w")
json.dump(length_desc, f)
f.close()