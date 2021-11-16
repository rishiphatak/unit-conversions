# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 09:32:49 2021

@author: Rishi2
"""

from helper import generateConvJson

graph = {}
graph['ft->in'] = 12
graph['in->cm'] = 2.54
graph['m->cm'] = 100
graph['km->m'] = 1000

generateConvJson("len_desc.json", graph, "len_conv.json")