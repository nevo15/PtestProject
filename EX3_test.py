
import pytest
import requests

base_url = "http://localhost:8000"

@pytest.fixture(scope="module")
def get_token():
    user = 'test'
    response = requests.post(base_url + '/token/' + user)
    return response.json()['token'], user


@pytest.fixture(scope="module")
def create_book():

    book = {"author": "Test",
            "pages": 182,
            "publisher": "Test",
            "sub_title": None,
            "title": "Test",
            "year": 2008}

    response = requests.post(base_url + '/books', json=book)
    return response.json()['id']


def test_delete_book(get_token, create_book):

    token , user = get_token

    delete_response = requests.delete(base_url + '/books/' + create_book, headers = {'user': user, 'token': token})
    get_book_id_response = requests.get(base_url+'/books/' + create_book)

    assert delete_response.status_code == 200
    assert get_book_id_response.status_code == 404

