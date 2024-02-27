class Company(object):
    def __init__(self, name, catchPhrase, bs):
        self.name = name
        self.catchPhrase = catchPhrase
        self.bs = bs

    def __eq__(self, other):
        if isinstance(other, Company):
            return (
                self.name == other.name
                and self.catchPhrase == other.catchPhrase
                and self.bs == other.bs
            )
        return False
