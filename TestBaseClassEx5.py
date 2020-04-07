import requests
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(filename="logger.log", level=logging.INFO)

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

        response = requests.post(self.url + "/books", json=book)


        logger.info("status code: {} ".format(response.status_code))
        logger.info("headers: {} ".format(response.headers))
        logger.info("text: {} ".format(response.text))
        logger.info("json: {} ".format(response.json()))
        logger.info("url: {} ".format(response.request.url))
        logger.info("method: {} ".format(response.request.method))
        logger.info("request headers: {} ".format(response.request.headers))
        logger.info("body: {} ".format(response.request.body))

        return response

    def post_token(self,user):
        return requests.post(self.url + "/token/" + user)


    def delete_book(self, book, token,user):
        return requests.delete(self.url + '/books/' + book, headers={'user': user, 'token': token})


