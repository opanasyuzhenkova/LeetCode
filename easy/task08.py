# 67. Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        fill_a = a.zfill(max_len)
        fill_b = b.zfill(max_len)
        add_bin = ""
        ten = 0

        for i in range(max_len-1, -1, -1):
            res_sum = ten
            res_sum += 1 if fill_a[i] == '1' else 0
            res_sum += 1 if fill_b[i] == '1' else 0
            add_bin = ('1' if res_sum % 2 == 1 else '0') + add_bin
            ten = 0 if res_sum < 2 else 1
        if ten != 0:
            add_bin = '1' + add_bin
            
        return add_bin


# Tricky Approaches

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2) + int(b,2))[2:]
    

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal_number = int(a,2) + int(b,2)
        return f"{decimal_number:b}"
    

print(Solution().addBinary("101", "1"))

    