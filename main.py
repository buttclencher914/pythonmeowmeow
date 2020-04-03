from MapAPI import Map
import numpy as np
import osmnx as ox
import networkx as nx
from sklearn.neighbors import KDTree
import matplotlib.pyplot as plt
import overpy as opy
import Djistra as rt
import over as dr


# Map.getNearestNodeByCoord(self,)


class mapCall:
    def getRoute(self, x1, y1, x2, y2):
        #k = ox.core.graph_from_file(r"C:\Users\User\.spyder-py3\data\map2.osm")
        dat = rt.perform(float(x1), float(y1), float(x2), float(y2))
        dis = dr.DisplayRoute()
        dis.display(dat[0], dat[1])
        
   



