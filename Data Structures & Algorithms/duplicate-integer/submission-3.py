class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # is_true = False
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if(nums[i]==nums[j]):
        #             is_true = True
        #             break
        # return is_true
        # agar arr sorted ho tb nhi toh two pointer will not work
        nums.sort()
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                return True
            i += 1
            j += 1
        return False