
class Pipeline():

    def __init__(self, name=None, stages=None):
        self.name = name
        self.stages = stages
        self.current_stage = 0

    def get_name(self):
        return self.name

    def current_stage(self):
        return self.stages[self.current_stage]

    def next_stage(self):
        if self.current_stage < len(self.stages) - 1:
            self.current_stage += 1

        return self.stages[self.current_stage]

    def previous_stage(self):
        if self.current_stage > 0:
            self.current_stage -= 1

        return self.stages[self.current_stage]