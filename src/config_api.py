import untangle
from src.Constants import PIPELINE_CONFIGURATION_URL
from src.api import Api


class ConfigApi(Api):

    def load_configuration(self):
        response = self.get_response(PIPELINE_CONFIGURATION_URL, method="GET")
        return untangle.parse(response)





