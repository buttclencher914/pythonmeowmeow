import sys

from osmread import parse_file, Way, Node
from math import sin, cos, radians, acos


class Map:
    def __init__(self):
        self.Nodes = {}

    def loadfromOSM(self, filename):
        filename = 'map2.osm'
        pf = parse_file(filename)
        for pd in pf:
            if isinstance(pd, Node):
                tn = SNode()
                tn.lat = pd.lat
                tn.lon = pd.lon
                tn.ID = pd.id
                tn.tags = pd.tags
                self.Nodes[tn.ID] = tn
        pf = parse_file(filename)
        for pd in pf:
            if isinstance(pd, Way):
                for n in pd.nodes:
                    if n not in self.Nodes:
                        continue
                    else:
                        for w in pd.nodes:
                            if n != w:
                                tw = SWay()
                                tw.ID = pd.id
                                tw.endNode = w
                                tw.tags = pd.tags
                                if w in self.Nodes:
                                    tnode1 = self.Nodes[n]
                                    tnode2 = self.Nodes[w]
                                    tw.cost = self.__getDistance(tnode1.lat, tnode1.lon, tnode2.lat, tnode2.lon)
                                if tw not in self.Nodes[n].ways:
                                    self.Nodes[n].ways.append(tw)

    @staticmethod
    def __getDistance(x1, y1, x2, y2):
        slat = radians(x1)
        slon = radians(y1)
        elat = radians(x2)
        elon = radians(y2)

        return 6371000 * (acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon)))

    def getNodesByCoord(self, lat, lon, radius=0):
        res = []
        for k in self.Nodes:
            n = self.Nodes[k]
            if self.__getDistance(n.lat, n.lon, lat, lon) <= radius:
                res.append(n)
        return res

    def getNearestNodeByCoord(self, lat, lon, radius=0):
        res = self.getNodesByCoord(lat, lon, radius)
        if len(res) == 0:
            return None
        comp = sys.maxsize
        ret = None
        for r in res:
            cal = self.__getDistance(lat, lon, r.lat, r.lon)
            if comp > cal:
                comp = cal
                ret = r
        return ret

    def getNodeByID(self, iden):
        if iden not in self.Nodes:
            return None
        else:
            return self.Nodes[iden]


class SNode:
    def __init__(self):
        self.lat = None
        self.lon = None
        self.ID = None
        self.tags = {}
        self.ways = []


class SWay:
    def __init__(self):
        self.endNode = None
        self.tags = {}
        self.ID = None
        self.cost = None
