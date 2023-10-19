import calclulator, pytest

def test_add():
    assert calclulator.add(5,3) == 8
    assert calclulator.add(12,7) == 19
    assert calclulator.add(22,20000) == 20022
    assert calclulator.add(-4,8) == 4

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calclulator.divide(10,0)
        
