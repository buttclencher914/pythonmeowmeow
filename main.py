
import Routing as rt
import DisplayRoute as dr





class mapCall:
    def getRoute(self, x1, y1, x2, y2):
        dat = rt.perform(float(x1), float(y1), float(x2), float(y2))
        dis = dr.DisplayRoute()
        dis.display(dat)
        
   
