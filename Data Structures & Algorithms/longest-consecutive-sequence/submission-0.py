class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            length = 1
            while x+1 in nums:
                x = x+1
                length=length+1
            if length>ans:
                ans = length
        return ans