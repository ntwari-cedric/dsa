class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        left =0
        right= 1
        while right < len(nums):
            if nums[left] != nums[right]:
                return nums[left]
            else:
                left+=2
                right +=2
        return nums[left]
        