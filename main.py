from MapAPI import Map
import numpy as np
import osmnx as ox
import networkx as nx
from sklearn.neighbors import KDTree
import matplotlib.pyplot as plt
import overpy as opy
import Djistra as dj



#Map.getNearestNodeByCoord(self,)




class mapCall:
    def getRoute(self,src,dst):
        

        
        orgin_point=(float(src[0]),float(src[1]))
        end_point=(float(dst[0]),float(dst[1]))
        
        k=ox.core.graph_from_file(r"C:\Users\User\.spyder-py3\data\Punggol.osm")
        sh=dj.perform(float(src[0]),float(src[1]),float(dst[0]),float(dst[1]))
        ox.plot_graph_route(k, sh, fig_height=10, fig_width=10,save=True,filename='PunggolPath',file_format='png')
        return 'PunggolPath.png'
#from Routing import perform
#perform(1.4017320, 103.9076350, 1.3990941, 103.9076522)
