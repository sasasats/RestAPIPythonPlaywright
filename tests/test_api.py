from playwright.sync_api import APIRequestContext
from http import HTTPStatus

from utils.ConverterUtils import *
from utils.RandomUtils import *
from models.Post import Post
from utils.Endpoints import Endpoint


def test_get_posts(api_request_context: APIRequestContext):
    response = api_request_context.get(Endpoint.POSTS.value)
    posts = get_posts_from_response(response)
    sorted_posts = sorted(posts)

    assert response.status == HTTPStatus.OK
    assert posts == sorted_posts


def test_get_post_99(api_request_context: APIRequestContext):
    response = api_request_context.get(Endpoint.POSTS.value + "99")
    post = get_post_from_response(response)

    assert response.status == HTTPStatus.OK
    assert post.userId == 10
    assert post.id == 99
    assert post.title != "" and post.body != ""


def test_get_post_150(api_request_context: APIRequestContext):
    response = api_request_context.get(Endpoint.POSTS.value + "150")

    assert response.status == HTTPStatus.NOT_FOUND
    assert response.json() == {}


def test_post_post(api_request_context: APIRequestContext):
    post = Post(1, get_random_number(12), get_random_string(10), get_random_string(50))
    response = api_request_context.post(Endpoint.POSTS.value, data=post.__dict__)
    response_post = get_post_from_response(response)

    assert post == response_post
    assert response_post.id != None
    assert response.status == HTTPStatus.CREATED


def test_get_users(api_request_context: APIRequestContext):
    response = api_request_context.get(Endpoint.USERS.value)
    users = get_users_from_response(response)
    template_user_5 = get_user_from_file("user5.json")

    assert response.status == HTTPStatus.OK
    assert users[4] == template_user_5


def test_get_user_5(api_request_context: APIRequestContext):
    response = api_request_context.get(Endpoint.USERS.value + "5")
    user = get_user_from_response(response)
    template_user_5 = get_user_from_file("user5.json")

    assert response.status == HTTPStatus.OK
    assert user == template_user_5
