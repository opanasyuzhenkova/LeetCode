# 26-Remove-Duplicates-from-Sorted-Array

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
        return j + 1
    
print(Solution().removeDuplicates([2, 2, 3, 3]))
        