
import pytest
import requests
from ProTest.TestBaseClassEx4 import APiRoutes

routes = APiRoutes()

@pytest.fixture(scope="module")
def get_token():
    user = 'test'
    response = routes.post_token(user)
    return response.json()['token'], user

@pytest.fixture(scope="module")
def create_book():
    response = routes.post_book()
    return response.json()['id']


def test_delete_book(get_token, create_book):

    token, user = get_token

    delete_response = routes.delete_book(create_book, token, user)
    get_book_id_response = routes.get_one_book(create_book)

    assert delete_response.status_code == 200
    assert get_book_id_response.status_code == 404

