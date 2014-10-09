import serial


class BoardController():

    def __init__(self):
        self.port = serial.Serial("/dev/tty.usbmodem1421", 9600)

    def read(self):
        message = self.port.readline()
        print " <== " + message
        return message

    def write(self, message):
        print " ==> " + message
        self.port.write(str(message))

