class Post(object):
    def __init__(self, userId, id, title, body):
        self.userId = userId
        self.id = id
        self.title = title
        self.body = body

    def __lt__(self, other):
        return self.id < other.id

    def __eq__(self, other):
        if isinstance(other, Post):
            return (
                self.userId == other.userId
                and self.title == other.title
                and self.body == other.body
            )
        return False
