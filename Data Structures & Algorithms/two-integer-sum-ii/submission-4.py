class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i]+numbers[j]== target:
        #             return [i+1, j+1]
        # return []

        # Binary search....
        n = len(numbers)
        for i in range(n-1):
            low, high = i+1, n-1
            temp = target - numbers[i]
            while low<=high:
                mid = (low+high)//2
                if numbers[mid] == temp:
                    return [i+1, mid+1]
                elif numbers[mid]<temp:
                    low = mid+1
                elif numbers[mid]>temp:
                    high = mid-1
        return []
