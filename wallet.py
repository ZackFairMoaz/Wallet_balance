class Wallet:
    def __init__(self):
        self._balance = 0

    def get_ammount(self):
        return self._balance

    def set_ammount(self, value):
        self._balance = value
        
    def remove_ammount(self, value):
        self._balance -= value 
