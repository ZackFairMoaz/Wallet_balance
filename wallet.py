class Wallet:
    def __init__(self):
        self._balance = 0

    def getAmount(self):
        return self._balance

    def setAmount(self, value):
        self._balance = value
        
    def removeAmount(self, value):
        self._balance -= value 
