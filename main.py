from MapAPI import Map

print("test")
m = Map()
m.loadfromOSM("map2.osm")
#all the codes below can work
#nodes = m.getNodesByCoord(1.4020051, 103.9060055, 20)
#nodes = m.getNodesByCoord(1.4020051, 103.9060055) #if radius is not specified, it is considered as 0
#node = m.getNearestNodeByCoord(1.4020051, 103.9060055)
#node = m.getNodeByID(id here)
node = m.getNearestNodeByCoord(1.4020051, 103.9060055, 20)

