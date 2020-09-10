# Main Memory of a IAS Computer

class MM():
    def __init__(self):
        self.memory = [['0']*40]*20

    def getData(self, loc):
        return self.memory[loc]

    def setData(self, loc, data):
        self.memory[loc] = data
