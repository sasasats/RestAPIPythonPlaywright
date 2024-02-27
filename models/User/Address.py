from models.User.Geo import Geo


class Address(object):
    def __init__(self, street, suite, city, zipcode, geo: Geo):
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode
        self.geo = geo

    def __eq__(self, other):
        if isinstance(other, Address):
            return (
                self.street == other.street
                and self.suite == other.suite
                and self.city == other.city
                and self.zipcode == other.zipcode
                and self.geo == other.geo
            )
        return False
