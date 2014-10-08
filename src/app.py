from src.board_controller import BoardController
from src.pipeline_controller import PipelineController


class PipelineApp():

    def __init__(self):
        self.controller = PipelineController()
        self.board = BoardController()

    def process_command(self, command):

        if command.startswith("CMD_READY"):
            print("key pressed")
            self.board.write("ACK")
            output = self.controller.current()
            print(output)
            self.reply(output)

        elif command.startswith("CMD_MODE"):
            print("switch between PIPELINE and STAGE modes")
            self.board.write("ACK")
            output = self.controller.switch_mode()
            print(output)
            self.reply(output)

        elif command.startswith("CMD_DEPLOY"):
            print("redeploy a selected STAGE or PIPELINE")
            self.board.write("ACK")
            output = self.controller.deploy()
            print(output)
            self.reply(output)

        elif command.startswith("CMD_DEPLOY_TO"):
            print("deploy to the NEXT STAGE in a pipeline")
            self.board.write("ACK")

        elif command.startswith("CMD_BACK"):
            print("scroll back through a stage or pipeline depending on current mode")
            self.board.write("ACK")
            output = self.controller.previous()
            print(output)
            self.reply(output)

        elif command.startswith("CMD_FORWARD"):
            print("scroll forward through a stage or pipeline depending on current mode")
            self.board.write("ACK")
            output = self.controller.next()
            print(output)
            self.reply(output)

        elif command.startswith("CMD_EXIT"):
            print("Exiting application")
            self.board.write("ACK")
            return False

        else:
            print("unknown command, please try again")
            self.board.write("ACK")
        return True

    def read_board(self):
        return self.board.read()

    def reply(self, message):
        counter = 0
        while counter < 10 and self.read_board() != "ACK":
            counter+=1
            self.board.write("DSP:LN2:SCR0:CMXA:" + message)


if __name__ == "__main__":
    app = PipelineApp()
    running = True
    while running:
        command = app.read_board()
        print command
        running = app.process_command(command)




