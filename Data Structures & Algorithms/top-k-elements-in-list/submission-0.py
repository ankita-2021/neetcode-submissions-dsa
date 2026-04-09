class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        # step 1: count frequency
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        result = []
        # step 2: k times find max frequency

        for _ in range(k):
            max_key = None
            max_freq = -1
            for key in freq:
                if freq[key] > max_freq:
                    max_freq = freq[key]
                    max_key = key
            result.append(max_key)
            freq[max_key] = -1
        return result

