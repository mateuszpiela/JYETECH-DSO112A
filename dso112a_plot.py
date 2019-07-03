import sys
import plotly
from plotly.graph_objs import Scatter, Layout

content = ""

list1 = list()
list2 = ""

with open(sys.argv[1] + ".csv",'r') as data:
    for line in data:
        if line.strip() == '--------------------------------------------------------------------------------------------------------' or line.strip() == '-------------------------------------------------------------------------------------------------------':
            break
    for line in data:
        list1.append(line)




lista2 = [elem.strip('\n') for elem in list1]
lista2 = [s.lstrip("0") for s in list2]


plotly.offline.plot({
    "data": [Scatter(y=list2)],
    "layout": {
        'xaxis': {'title': 'Time'},
        'yaxis': {'title': 'Volts', 'autorange': True},
        'title': 'Oscilloscope'
        }
}, filename=sys.argv[1] + ".html")
