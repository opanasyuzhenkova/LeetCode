# 69. Sqrt(x)

class Solution:
    def mySqrt(self, x: int) -> int:
        a = 0
        b = 0
        while b >= 0:
           a += 1
           b = x - a**2
        return a-1
    
print(Solution().mySqrt(8))
