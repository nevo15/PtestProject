import requests
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(filename="logger.log",level=logging.INFO)


class ApiClient(requests.Session):
    def __init__(self):
        super(ApiClient, self).__init__()  # initialises parent class; in Python 3: super().__init__()
        self.hooks['response'].append(self._log_details)  # for every response the _log_details() method will be called

    @staticmethod
    def _log_details(response, *args, **kwargs):
        logger.info("status code: {} ".format(response.status_code))
        logger.info("headers: {} ".format(response.headers))
        logger.info("text: {} ".format(response.text))
        logger.info("url: {} ".format(response.request.url))
        logger.info("method: {} ".format(response.request.method))
        logger.info("request headers: {} ".format(response.request.headers))
        logger.info("body: {} ".format(response.request.body))


class APiRoutes(ApiClient):
    def __init__(self):
        super(APiRoutes,self).__init__()
        self.url = "http://localhost:8000"

    def get_knockknock(self):
        return self.get(self.url + "/knockknock")

    def get_books(self):
        return self.get(self.url + "/books")

    def get_one_book(self,book):
        return self.get(self.url + "/books/" + book)

    def post_book(self):
        book = {"author": "Test",
                "pages": 182,
                "publisher": "Test",
                "sub_title": None,
                "title": "Test",
                "year": 2008}

        res = self.post(self.url + "/books", json=book)
        return res


    def post_token(self,user):
        return self.post(self.url + "/token/" + user)


    def delete_book(self, book, token,user):
        return self.delete(self.url + '/books/' + book, headers={'user': user, 'token': token})
