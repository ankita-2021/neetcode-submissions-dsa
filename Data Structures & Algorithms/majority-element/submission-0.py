class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count1 = len(nums)/2
        res = 0
        for i in range(len(nums)):
            total = nums.count(nums[i])
            if total>count1:
                res = nums[i]
                break
        return res
