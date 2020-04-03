from MapAPI import Map
import numpy as np
import osmnx as ox
import networkx as nx
from sklearn.neighbors import KDTree
import matplotlib.pyplot as plt
import overpy as opy
import Routing as rt
import DisplayRoute as dr


# Map.getNearestNodeByCoord(self,)


class mapCall:
    def getRoute(self, x1, y1, x2, y2):
        k = ox.core.graph_from_file(r"C:\Users\Ian\Documents\GitHub\pythonmeowmeow\Punggol.osm")
        sh = rt.perform(x1, y1, x2, y2)
        ox.plot_graph_route(k, sh, fig_height=10, fig_width=10, save=True, filename='PunggolPath', file_format='png')
        return 'PunggolPath.png'


# ff = mapCall()
# ff.getRoute(1.4014434, 103.9082113, 1.3997726, 103.9116292)
dat = rt.perform(1.4014434, 103.9082113, 1.3997726, 103.9116292)
dis = dr.DisplayRoute()
dis.display(dat)
# from Routing import perform
# perform(1.4017320, 103.9076350, 1.3990941, 103.9076522)
