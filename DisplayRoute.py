import webbrowser


class DisplayRoute:
    def display(self, nodelist, waylist):
        url = "https://overpass-turbo.eu/map.html?Q=%5Bout%3Ajson%5D%5Btimeout%3A25%5D%3B("
        for n in nodelist:
            url += "node(" + str(n) + ")%3B"
        for w in waylist:
            url += "way(" + str(w) + ")%3B"
        url += ")%3Bout%20geom%3B"
        webbrowser.open(url, new=0, autoraise=True)
