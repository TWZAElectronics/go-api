from src.Constants import PIPELINE_SCHEDULE_TEMPLATE
from src.api import Api


class PipelineApi(Api):

    def schedule_pipeline(self, pipeline_name):
        url = PIPELINE_SCHEDULE_TEMPLATE.format(pipeline_name)
        return self.get_response(url)





