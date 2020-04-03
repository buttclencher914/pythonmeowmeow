import webbrowser


class DisplayRoute:
    def display(self, nodelist):
        url = "http://overpass-turbo.eu/map.html?Q=node(id%3A"
        for n in nodelist:
            url += str(n) + "%2C"
        url = url[:-3]
        url += ")%3Bway%5Bhighway%5D(bn)%3Bout%20geom%3B"
        webbrowser.open(url, new=0, autoraise=True)
