from requests import Request, Session
import logging


class Endpoint:
    """
    Represent REST API endpoint
    """

    def __init__(self, endpoint: str):
        """
        Initialize REST API
        """
        self._endpoint = endpoint
        self._session = Session()

    def run(self, resource: str, method: str, **data):
        """
        Execute REST API call
        """
        req = Request(method=method, **data)
        req.url = self._endpoint + resource
        prepared = req.prepare()
        try:
            result = self._session.send(prepared, verify=False)
            return result
        except ConnectionError as ex:
            logging.warning("Connection error: ", ex)
