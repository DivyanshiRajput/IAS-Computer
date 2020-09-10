# Program Control Unit of a IAS Computer

# Instruction Buffer Register
class IBR():
    def __init__(self):
        self.data = ['0']*20

    def getData(self):
        return self.data

    def setInstruction (self, data):
        self.data = data[20:40]

    def reset(self):
        self.data = ["0"]*20


# Program Counter
class PC():

    def __init__(self):
        self.address = 0

    def incrementPC(self):
        self.address += 1


# Instruction Register
class IR():
    def __init__(self):
        self.opcode = ['0']*8

    def getOpcode(self):
        return self.opcode

    def setOpcode(self, data):
        self.opcode = data[0:8]


# Memory Address Register
class MAR():
    def __init__(self):
        self.address = ['0']*12

    def getAddress(self):
        return self.address

    def setAddress(self, data):
        self.address = data[8:20]
