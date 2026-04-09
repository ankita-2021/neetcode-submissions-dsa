class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]: 
        from collections import Counter  
        count = Counter(nums)  
        major = len(nums)//3
        res = []
        for num in count:
            if count[num] > major: 
                res.append(num)
        return res
