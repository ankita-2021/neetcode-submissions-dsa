class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # while val in nums:
        #     nums.remove(val)
        # return len(nums)

        for i in range(len(nums)):
            if val in nums:
                nums.remove(val)
        return len(nums)