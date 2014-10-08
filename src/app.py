from src.pipeline_controller import PipelineController


class PipelineApp():

    def __init__(self):
        self.controller = PipelineController()

    def process_command(self, command):

        if command == "CMD_READY":
            print("key pressed")
            print(self.controller.current())

        elif command == "CMD_MODE":
            print("switch between PIPELINE and STAGE modes")
            print(self.controller.switch_mode())

        elif command == "CMD_DEPLOY":
            print("redeploy a selected STAGE or PIPELINE")
            print(self.controller.deploy())

        elif command == "CMD_DEPLOY_TO":
            print("deploy to the NEXT STAGE in a pipeline")

        elif command == "CMD_BACK":
            print("scroll back through a stage or pipeline depending on current mode")
            print(self.controller.previous())

        elif command == "CMD_FORWARD":
            print("scroll forward through a stage or pipeline depending on current mode")
            print(self.controller.next())

        elif command == "exit":
            print("Exiting application")
            return False

        else:
            print("unknown command, please try again")
        return True


if __name__ == "__main__":
    app = PipelineApp()
    running = True
    while running:
        running = app.process_command(raw_input())




