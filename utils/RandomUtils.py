import random
import string


def get_random_number(range: int):
    return random.randint(1, range)


def get_random_string(length: int):
    letters = string.ascii_letters
    return "".join(random.choice(letters) for _ in range(length))
