from src.config_api import ConfigApi
from src.pipeline import Pipeline
from src.pipeline_api import PipelineApi


class PipelineController():

    def __init__(self):
        self.mode = PipelineMode.PIPELINE_MODE
        self.configuration = ConfigApi().load_configuration()
        self._setup_pipelines()
        self.current_pipeline = 0
        
    def current(self):
        if self.mode == PipelineMode.PIPELINE_MODE:
            return self.pipelines.values()[self.current_pipeline].get_name()

        return self.pipelines.values()[self.current_pipeline].current_stage()

    def next(self):
        if self.mode == PipelineMode.PIPELINE_MODE:
            if self.current_pipeline < len(self.pipelines) - 1:
                self.current_pipeline += 1

            return self.pipelines.values()[self.current_pipeline].get_name()

        return self.pipelines.values()[self.current_pipeline].next_stage()

    def previous(self):
        if self.mode == PipelineMode.PIPELINE_MODE:
            if self.current_pipeline > 0:
                self.current_pipeline -= 1

            return self.pipelines.values()[self.current_pipeline].get_name()

        return self.pipelines.values()[self.current_pipeline].previous_stage()

    def switch_mode(self):
        if self.mode == PipelineMode.PIPELINE_MODE:
            self.mode = PipelineMode.STAGE_MODE
        else:
            self.mode = PipelineMode.PIPELINE_MODE

        return self.mode

    def deploy(self):
        if self.mode == PipelineMode.PIPELINE_MODE:
            api = PipelineApi()
            return api.schedule_pipeline(self.pipelines.values()[self.current_pipeline].get_name())

        return "functionality not available yet for stages"

    def _setup_pipelines(self):
        self.pipelines = {}
        print self.configuration
        for pipeline_group in self.configuration.cruise.pipelines:
            for pipeline in pipeline_group.pipeline:
                stages = []
                for stage in pipeline.stage:
                    pipeline_name = pipeline.get_attribute("name")
                    stages.append(stage.get_attribute("name"))
                self.pipelines[pipeline_name] = Pipeline(pipeline_name, stages)


class PipelineMode():
    PIPELINE_MODE = "PIPELINE"
    STAGE_MODE = "STAGE"
