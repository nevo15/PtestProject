import requests


class APiRoutes:
    def __init__(self):
        self.url = "http://localhost:8000"

    def get_knockknock(self):
        return requests.get(self.url + "/knockknock")

    def get_books(self):
        return requests.get(self.url + "/books")

    def get_one_book(self,book):
        return requests.get(self.url + "/books/" + book)

    def post_book(self):
        book = {"author": "Test",
                "pages": 182,
                "publisher": "Test",
                "sub_title": None,
                "title": "Test",
                "year": 2008}
        return requests.post(self.url + "/books", json=book)


    def post_token(self,user):
        return requests.post(self.url + "/token/" + user)


    def delete_book(self, book, token,user):
        return requests.delete(self.url + '/books/' + book, headers={'user': user, 'token': token})
