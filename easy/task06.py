# 58. Length of Last Word

class Solution:
    def lengthofLastWord(self, s: str) -> int:
        l_str = list(s.strip().split(' '))
        return len(l_str[-1])


print(Solution().lengthofLastWord("fly me   to   the moon"))
