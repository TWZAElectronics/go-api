from src.board_controller import BoardController
from src.pipeline_controller import PipelineController


class PipelineApp():

    def __init__(self):
        self.controller = PipelineController()
        self.board = BoardController()

    def process_command(self, command):

        if command == "CMD_READY":
            print("key pressed")
            output = self.controller.current()
            print(output)
            self.reply(output)

        elif command == "CMD_MODE":
            print("switch between PIPELINE and STAGE modes")
            output = self.controller.switch_mode()
            print(output)
            self.reply(output)

        elif command == "CMD_DEPLOY":
            print("redeploy a selected STAGE or PIPELINE")
            output = self.controller.deploy()
            print(output)
            self.reply(output)

        elif command == "CMD_DEPLOY_TO":
            print("deploy to the NEXT STAGE in a pipeline")

        elif command == "CMD_BACK":
            print("scroll back through a stage or pipeline depending on current mode")
            output = self.controller.previous()
            print(output)
            self.reply(output)

        elif command == "CMD_FORWARD":
            print("scroll forward through a stage or pipeline depending on current mode")
            output = self.controller.next()
            print(output)
            self.reply(output)

        elif command == "exit":
            print("Exiting application")
            return False

        else:
            print("unknown command, please try again")
        return True

    def read_board(self):
        return self.board.read()

    def reply(self, message):
        self.board.write("ACK")
        self.board.write(message)


if __name__ == "__main__":
    app = PipelineApp()
    running = True
    while running:
        command = app.read_board()
        running = app.process_command(command)




