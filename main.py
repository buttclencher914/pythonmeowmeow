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
    def getRoute(self, x1, y1, x2, y2, mapapiobject):
        #k = ox.core.graph_from_file(r"C:\Users\User\.spyder-py3\data\map2.osm")
        dat = rt.perform(float(x1), float(y1), float(x2), float(y2), mapapiobject)
        dis = dr.DisplayRoute()
        dis.display(dat)

m = Map()
m.loadfromOSM("map2.osm")
mc = mapCall()
mc.getRoute(0,0,0,0, m)
        
   



