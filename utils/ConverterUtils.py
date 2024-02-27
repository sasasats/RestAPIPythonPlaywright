import json
from playwright.sync_api import APIResponse

from models.Post import Post
from models.User.User import User

BASE_FILE_PATH = "./src/jsons/"

def get_posts_from_response(response: APIResponse):
    return [Post(**post_data) for post_data in json.loads(response.text())]

def get_post_from_response(response: APIResponse):
    return Post(**json.loads(response.text()))

def get_users_from_response(response: APIResponse):
    return [User(**user_data) for user_data in json.loads(response.text())]

def get_user_from_response(response: APIResponse):
    return User(**json.loads(response.text()))

def get_user_from_file(file_path):
    with open(BASE_FILE_PATH + file_path, "r") as file:
        data = json.load(file)

    return User(**data)