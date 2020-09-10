# Arithmatic Logic Unit of a IAS Computer

# Accumulator
class AC():

    def __init__(self):
        self.data = ['0']*40

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data


# Multiplier / Quotient
class MQ():

    def __init__(self):
        self.data = ['0']*40

    def setData (self):
        self.data = data

    def getData(self):
        return self.data


# Arithmatic Logic Circuits
class ALC():
    def ADD(self, MBR, AC):
        val = binToDec(MBR.getBuffer()) + binToDec(AC.getData())
        newVal = decToBin(val)
        AC.setData(padding(newVal, 40))

    def SUB(self, MBR, AC):
        val = binToDec(MBR.getBuffer()) - binToDec(AC.getData())
        newVal = decToBin(val)
        AC.setData(padding(newVal, 40))

    def LOAD (self, MBR,AC):
        AC.setData(MBR.getBuffer())

    def STORE (self, MBR, AC):
        MBR.setBuffer(AC.getData())


# Memory Buffer Register
class MBR():

    def __init__(self):
        self.buffer = ['0']*40

    def getBuffer(self):
        return self.buffer

    def setBuffer(self, buffer):
        self.buffer = buffer


# FUNCTIONS
def decToBin(n): #function for converting decimal to binary
    b = []
    while(n>0):
        b.append(str(n%2))
        n = n//2
    b = b[::-1]
    return b


def binToDec(l): #function for converting binary to decimal
    l = l[::-1]
    j = 0
    temp = 0
    for i in l:
        temp += int(i)*pow(2,j)
        j += 1
    return temp

def padding(list, n): #funtion for adding padding to the converted binary list
    l = len(list)
    for i in range(n-l):
        list.insert(0,'0')
    return list
