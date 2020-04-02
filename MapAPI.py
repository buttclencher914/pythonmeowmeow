# Written by Yu Ding Xiang Ian, ID:1902622
import sys

from osmread import parse_file
from math import sin, cos, radians, acos
from typing import List


class SNode:  # single node object
    def __init__(self):
        self.lat = None
        self.lon = None
        self.ID = None
        self.generated = False  # if its not from the map but generated as an abstract node(doesnt exist)
        self.tags = {}
        self.ways = []


class SWay:  # single way object that can belong to node.ways[] object
    def __init__(self):
        self.endNode = None
        self.tags = {}
        self.ID = None
        self.cost = 0
        self.route = False  # if its specified in the relation
        self.generated = False  # if its not from the map but generated as an abstract way(doesnt exist)


class Map:
    def __init__(self):
        self.Nodes = {}

    def loadfromOSM(self, filename):
        ignore_types = ['restriction', 'enforcement', 'boundary']  # tags to ignore for relation
        relations = {}
        ways = {}
        pf = parse_file(filename)
        for pd in pf:
            typ = self.__getTypeValue(type(pd))  # return 1 for node, 2 for way, 3 for relation
            if typ == 1:
                tn = SNode()
                tn.lat = pd.lat
                tn.lon = pd.lon
                tn.ID = pd.id
                tn.tags = pd.tags
                self.Nodes[tn.ID] = tn  # add node into the object
            elif typ == 2:  # if its a way
                narr = []
                for n in pd.nodes:  # will append node into into the way dictionary if it exists
                    if n not in self.Nodes:
                        continue
                    else:
                        srm = _SRouteMember()
                        srm.UID = n
                        narr.append(srm)
                way = _Ways()
                way.tags = pd.tags
                way.members = narr
                ways[pd.id] = way  # ways are added here
            else:  # if relation
                if pd.tags['type'] not in ignore_types:
                    members = []
                    for m in pd.members:
                        tmem = _SRouteMember()
                        tmem.type = m.type
                        tmem.UID = m.member_id
                        members.append(tmem)
                    sroute = _SRoute()
                    sroute.tags = pd.tags
                    sroute.members = members
                    relations[pd.id] = sroute  # relations are added here
        pf.close()
        nrelations = {}  # variable to store relations that contain ways and nodes
        rrelations = {}  # variable to store relations that contain relations
        for key in relations:  # splitting is done here
            fin = []
            for member in relations[key].members:
                rel_mode = False
                if str(member.type).__contains__('Relation'):
                    rel_mode = True
                rm = _SRouteMember()
                rm.UID = member.UID
                rm.type = member.type
                fin.append(rm)

            st = _SRoute()
            st.tags = relations[key].tags
            st.members = fin
            if rel_mode:
                rrelations[key] = st
            else:
                nrelations[key] = st
        del relations  # free up some precious memory

        for key in rrelations:  # now to combine relations together(which are made up of ways and nodes)
            fin = []
            for mem in rrelations[key].members:
                if mem in nrelations:
                    fin += nrelations[mem.members]
                    del nrelations[mem.members]
            if len(fin) != 0:
                nrelations[key].members = fin

        # nodes are points and ways are connections
        # according to some relations, there are nodes that are connected to each other without anything in between
        # likewise for ways
        # fixing that by adding nodes in between connecting ways, and likewise for connecting nodes
        a_node_count = 0
        a_way_count = 0
        comarr = []
        for route in nrelations.values():  # iterate for every combined relation
            arrlen = len(route.members)
            arr = []
            for i in range(arrlen):
                if i != (arrlen - 1):
                    mem1 = route.members[i]
                    mem2 = route.members[i + 1]
                    t1 = self.__getTypeValue(mem1.type)
                    t2 = self.__getTypeValue(mem2.type)
                    t3 = t1 + t2
                    if t3 == 4:  # if its way - way
                        anode = SNode()  # adding a node in between
                        anode.generated = True
                        anode.ID = a_node_count
                        anode.tags = route.tags
                        self.Nodes[anode.ID] = anode
                        arr.append((mem1.UID, 2))
                        arr.append((anode.ID, 1))
                        if mem1.UID not in ways:
                            sr = _SRoute()
                            sr.tags = route.tags  # give it a tag
                            ways[mem1.UID] = sr
                        a_node_count -= 1
                    elif t3 == 3:  # if its node-way or way-node
                        continue  # no problem so nothing to fix
                    else:  # if its node-node
                        sr = _SRoute()  # adding a way in between
                        sr.tags = route.tags
                        ways[a_way_count] = sr
                        arr.append((mem1.UID, 1))
                        arr.append((a_way_count, 2))
                        if mem1.UID not in self.Nodes:
                            anode = SNode()
                            anode.ID = mem1.UID
                            anode.generated = True
                            anode.tags = route.tags
                            self.Nodes[mem1.UID] = anode
                        a_way_count -= 1
            comarr.append(arr)  # storing the ids in an array completed[ relation[ tuple(ID, type), ...], ...]

        for arr in comarr:  # now to link the nodes together with the ways in between
            if len(arr) >= 3:
                for i in range(2, len(arr)):
                    com1 = arr[i - 2]
                    com2 = arr[i]
                    if com1[1] == 1:  # if n element is a node, then n+2 element is the next node
                        sw = SWay()
                        sw.ID = arr[i - 1][0]  # copy the id of the ways in between the nodes
                        sw.tags = self.Nodes[com1[0]].tags  # inherit the tags from node
                        sw.generated = True
                        sw.route = True
                        sw.endNode = com2[0]
                        self.Nodes[com1[0]].ways.append(sw)
        # now to link up the nodes and ways together that are actually connected but not specified by relation
        for e in ways:
            members = ways[e].members
            for n in members:
                for w in members:
                    if n != w:
                        tw = SWay()
                        tw.ID = e
                        tw.endNode = w.UID
                        tw.route = w.route
                        tw.generated = w.generated
                        tw.tags = ways[e].tags
                        if w.UID in self.Nodes.keys():
                            tnode1 = self.Nodes[n.UID]
                            tnode2 = self.Nodes[w.UID]
                            tw.cost = self.getDistance(tnode1.lat, tnode1.lon, tnode2.lat, tnode2.lon)
                        tn = self.Nodes[n.UID]
                        if tw not in tn.ways and not tn.generated:
                            self.Nodes[n.UID].ways.append(tw)

    def getDistance(self, x1, y1, x2, y2):  # calculate distance in meters between 2 coords
        if x1 == x2 and y1 == y2:
            return 0
        else:
            slat = radians(x1)
            slon = radians(y1)
            elat = radians(x2)
            elon = radians(y2)
            return 6371000 * (acos(sin(slat) * sin(elat) + cos(slat) * cos(elat) * cos(slon - elon)))

    @staticmethod
    def __getTypeValue(typ):  # returns 1 if node, 2 if way, 3 if relation
        typs = str(typ)
        if typs.__contains__('Node'):
            return 1
        elif typs.__contains__('Way'):
            return 2
        else:
            return 0

    def getNodesByCoord(self, lat, lon, radius=0) -> List[SNode]:  # gets array of nodes in the coords
        res = []
        for k in self.Nodes:
            n = self.Nodes[k]
            if n.generated:
                continue
            if self.getDistance(n.lat, n.lon, lat, lon) <= radius:
                res.append(n)
        return res

    def getNearestNodeByCoord(self, lat, lon, radius=0) -> SNode:  # will get a node closest to the coord, radius = search area
        res = self.getNodesByCoord(lat, lon, radius)
        if len(res) == 0:
            return None
        comp = sys.maxsize
        ret = None
        for r in res:
            cal = self.getDistance(lat, lon, r.lat, r.lon)
            if comp > cal:
                comp = cal
                ret = r
        return ret

    def getNodeByID(self, iden) -> SNode:  # self-explanatory
        if iden not in self.Nodes:
            return None
        else:
            return self.Nodes[iden]


class _SRoute:  # private class
    def __init__(self):
        self.tags = {}
        self.members = []


class _Ways(_SRoute):
    def __init__(self):
        super().__init__()


class _SRouteMember:
    def __init__(self):
        self.type = None
        self.UID = None
        self.route = False
        self.generated = False
