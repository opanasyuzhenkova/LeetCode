# 27-Remove-Element

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                slow += 1
                nums[slow] = nums[fast]
        return slow 
    
print(Solution().removeElement([3, 2, 2, 3, 3], 3))
