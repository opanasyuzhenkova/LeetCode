# 443. String Compression

class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        i = 0
        j = 0
        while i < n:
            count = 1
            while i < n - 1 and chars[i] == chars[i + 1]:
                count += 1
                i += 1

            chars[j] = chars[j]
            j += 1
            if count > 1:
                for c in str(count):
                    chars[j] = c 
                    j += 1
            i += 1
        return j
    
    
test = Solution()
print(test.compress(["a","a","b","b","c","c","c"]))
