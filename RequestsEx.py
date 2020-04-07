import json
import requests

base_url = "http://localhost:8000"


def print_get_routes():
    response = requests.get(base_url + "/knockknock")
    print(response.url)
    print(response.status_code)
    print(response.text)

    response = requests.get(base_url + "/books")
    print(response.url)
    print(response.status_code)
    parsed = response.json()
    print(json.dumps(parsed, indent=2))

    response = requests.get(base_url + "/books/9b30d321-d242-444f-b2db-884d04a4d806")
    print(response.url)
    parsed = response.json()
    print(json.dumps(parsed, indent=2))


def print_post_routes():
    book = {"author": "Test",
            "pages": 182,
            "publisher": "Test",
            "sub_title": None,
            "title": "Test",
            "year": 2008}

    response = requests.post(base_url + "/books", json=book)
    print(response.url)
    print(response.status_code)
    parsed = response.json()
    print(json.dumps(parsed, indent=2))

    response = requests.post(base_url + "/token/UseR")
    print(response.url)
    print(response.status_code)
    parsed = response.json()
    print(json.dumps(parsed, indent=2))




if __name__ == '__main__':
    print_get_routes()
    print_post_routes()


