# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 09:42:36 2021

@author: Rishi2
"""

from helper import generateConvJson

graph = {}
graph['centuries->years'] = 100
graph['years->months'] = 12
graph['years->days'] = 365
graph['weeks->days'] = 7
graph['days->hours'] = 24
graph['hours->minutes'] = 60
graph['minutes->s'] = 60
graph["s->ms"] = 1000
graph['ms->ns'] = 1000000

generateConvJson("time_desc.json", graph, "time_conv.json")