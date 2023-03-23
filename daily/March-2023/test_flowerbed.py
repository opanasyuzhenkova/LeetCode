from task20 import Flowerbed

def test_flower_begining():
    assert Flowerbed().canPlaceFlowers([0,0,1,0,1], 1) == True
def test_flower_begining():
    assert Flowerbed().canPlaceFlowers([0,0,0,1,0,1], 2) == False
def test_flower_at_the_end():
    assert Flowerbed().canPlaceFlowers([1,0,1,0,0,0], 1) == True
def test_flower_at_the_end_2():
    assert Flowerbed().canPlaceFlowers([1,0,1,1,0,0], 1) == True
    