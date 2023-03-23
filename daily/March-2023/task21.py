# 2348. Number of Zero-Filled Subarrays

class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        cnt_zero_subarrays = cur_zero_subarrays = 0     
        for num in nums:
            if num == 0:
                cur_zero_subarrays += 1
                cnt_zero_subarrays += cur_zero_subarrays
            else:
                cur_zero_subarrays = 0    
        return cnt_zero_subarrays
    

print(Solution().zeroFilledSubarray(nums = [1,3,0,0,2,0,0,4]))
