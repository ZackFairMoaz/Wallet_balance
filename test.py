from wallet import Wallet

def test_getAmount():
    obj=Wallet()
    obj.setAmount(20)
    assert obj.getAmount()==20

def test_getAmount():
    obj=Wallet()
    obj.setAmount(300)
    assert obj.getAmount()==300
