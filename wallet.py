class Wallet:
    def __init__(self):
        self._balance = 0

    def getAmmount(self):
        return self._balance

    def setAmmount(self, value):
        self._balance = value
        
    def removeAmmount(self, value):
        self._balance -= value 
