class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # t.c = O(n^2), S.c = O(1)
        # ans = 0
        # for x in nums:
        #     length = 1
        #     while x+1 in nums:
        #         x = x+1
        #         length=length+1
        #     if length>ans:
        #         ans = length
        # return ans

        # using hashset
        numSet = set(nums)
        longest  = 0
        for nums in numSet:
            if (nums-1) not in numSet:
                length = 1
                while (nums + length) in numSet:
                    length+=1
                longest = max(length, longest)
        return longest
