# 66. Plus One

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        result = 0
        for number in digits:
            result = result  * 10 + number

        result += 1
        result = str(result)
        return list(map(int, result))


print(Solution().plusOne(digits = [1, 2, 3]))
