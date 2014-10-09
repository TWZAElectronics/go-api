import time
from src.board_controller import BoardController
from src.pipeline_controller import PipelineController


class PipelineApp():

    def __init__(self):
        self.controller = PipelineController()
        self.board = BoardController()

    def process_command(self, command):
        if command.startswith("CMD_READY"):
            output = self.controller.current()
            print(output)
            self.reply(output)

        elif command.startswith("CMD_MODE"):
            print("switch between PIPELINE and STAGE modes")
            output = self.controller.switch_mode()
            print(output)
            self.reply(output)

        elif command.startswith("CMD_DEPLOY"):
            print("redeploy a selected STAGE or PIPELINE")
            output = self.controller.deploy()
            print(output)
            self.reply(output)

        elif command.startswith("CMD_DEPLOY_TO"):
            print("deploy to the NEXT STAGE in a pipeline")

        elif command.startswith("CMD_BACK"):
            print("scroll back through a stage or pipeline depending on current mode")
            output = self.controller.previous()
            print(output)
            self.reply(output)

        elif command.startswith("CMD_FORWARD"):
            print("scroll forward through a stage or pipeline depending on current mode")
            output = self.controller.next()
            print(output)
            self.reply(output)

        elif command.startswith("CMD_EXIT"):
            print("Exiting application")
            return False

        else:
            print("unknown command, please try again")
        return True

    def read_board(self):
        return self.board.read()

    def reply(self, message):
        self.board.write("DSP:LN1:SCR1:CMXRBGGGG:" + message)
        time.sleep(1)

if __name__ == "__main__":
    app = PipelineApp()
    running = True
    while running:
        command = app.read_board()
        running = app.process_command(command)




