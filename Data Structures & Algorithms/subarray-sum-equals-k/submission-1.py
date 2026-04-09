class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # #brute force
        # count = 0
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i, len(nums)):
        #         sum+=nums[j]
        #         if sum == k:
        #             count+=1
        # return count

        # hashmap + prefix sum
        prefix_sum =0
        count = 0
        mp = {0:1} # imp
        for i in range(len(nums)):
            prefix_sum+=nums[i]
            if prefix_sum-k in mp:
                count+=mp[prefix_sum-k]
            if prefix_sum in mp:
                mp[prefix_sum]+=1
            else:
                mp[prefix_sum]=1
        return count

            
                

