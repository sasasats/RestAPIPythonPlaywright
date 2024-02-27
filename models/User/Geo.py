class Geo(object):
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def __eq__(self, other):
        if isinstance(other, Geo):
            return self.lat == other.lat and self.lng == other.lng
        return False
