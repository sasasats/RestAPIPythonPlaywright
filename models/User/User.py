from models.User.Address import Address
from models.User.Company import Company


class User(object):
    def __init__(
        self,
        id,
        name,
        username,
        email,
        address: Address,
        phone,
        website,
        company: Company,
    ):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.address = Address(**address)
        self.phone = phone
        self.website = website
        self.company = Company(**company)

    def __eq__(self, other):
        if isinstance(other, User):
            return (
                self.id == other.id
                and self.name == other.name
                and self.username == other.username
                and self.email == other.email
                and self.address == other.address
                and self.phone == other.phone
                and self.website == other.website
                and self.company == other.company
            )
        return False
