# 605. Can Place Flowers

class Flowerbed:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (flowerbed[i - 1] == 0 or i == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                n -= 1
                flowerbed[i] = 1
        if n > 0: 
            return False
        else: return True


print(Flowerbed().canPlaceFlowers([0,0,1,0,0], 1))
