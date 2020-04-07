
import requests

base_url = "http://localhost:8000"

def test_get_knockknock():

    response = requests.get(base_url + "/knockknock")

    assert response.status_code == 200
    assert response.text == "Who's there?"

def test_get_books():

    response = requests.get(base_url + "/books")

    assert response.status_code == 200
    assert response.json() is not None


def test_get_one_book():
    response = requests.get(base_url + "/books/9b30d321-d242-444f-b2db-884d04a4d806")
    assert response.status_code == 200
    assert response.json() == {'author': 'Gerald Weinberg',
                                'id': '9b30d321-d242-444f-b2db-884d04a4d806',
                                'pages': 182,
                                'publisher': 'Dorset House Publishing',
                                'sub_title': None,
                                'title': 'Perfect Software And Other Illusions About Testing',
                                'year': 2008}


def test_post_book():

    book = {"author": "Test",
            "pages": 182,
            "publisher": "Test",
            "sub_title": None,
            "title": "Test",
            "year": 2008}

    response = requests.post(base_url + "/books", json=book)
    assert response.status_code == 201
    assert response.json()['id'] is not None


def test_post_token():
    response = requests.post(base_url + "/token/UseR")
    assert response.status_code == 201
    assert response.json() is not None


