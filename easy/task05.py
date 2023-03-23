# 35. Search Insert Position

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            min_dif = nums[-1]
            min_ind = len(nums)
            for i in range(len(nums)):
                if abs(nums[i] - target) <= min_dif:
                    min_dif = abs(nums[i] - target)
                    min_ind = i
            if target > nums[min_ind]:
                return min_ind + 1
            else:
                return min_ind

print(Solution().searchInsert(nums=[1,3,5,6], target=5))