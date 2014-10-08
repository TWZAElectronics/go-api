import httplib
from src.Constants import GO_PIPELINE_URL, GO_PIPELINE_PORT


class Api():

    def __init__(self):
        pass

    def get_response(self, url, method="POST"):
        conn = httplib.HTTPConnection(GO_PIPELINE_URL, GO_PIPELINE_PORT)
        conn.request(method, url)
        response = conn.getresponse()
        return response.read()
