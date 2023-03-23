# 28. Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1
    
                    
print(Solution().strStr(haystack = "sadbutsad", needle = "sad"))
