class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for ch1, ch2 in zip(word1, word2):
            res+=ch1
            res+=ch2
        res+=word1[len(word2):]
        res+=word2[len(word1):]
        return res
        