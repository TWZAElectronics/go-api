import serial


class BoardController():

    def __init__(self):
        self.port = serial.Serial("/dev/tty.usbmodem1421", 9600)

    def read(self):
        return self.port.readline()

    def write(self, message):
        self.port.write(message)

