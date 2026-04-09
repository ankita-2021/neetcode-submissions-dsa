class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]: 
        from collections import Counter  
        count = Counter(nums)  
        major = len(nums)//3
        res = []
        for i in count:
            if count[i] > major: 
                res.append(i)
        return res
