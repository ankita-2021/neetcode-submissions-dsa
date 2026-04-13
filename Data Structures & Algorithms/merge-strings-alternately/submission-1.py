class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # # t.c = O(n+m), s.c = O(n+m) , worst case = O((n+m)^2)
        # res = ""
        # for ch1, ch2 in zip(word1, word2):
        #     res+=ch1
        #     res+=ch2
        # res+=word1[len(word2):]
        # res+=word2[len(word1):]
        # return res

        # ...........................................
        # zip use krke thoda better version
        res = []
        for ch1, ch2 in zip(word1, word2):
            res.append(ch1)
            res.append(ch2)
        res.append(word1[len(word2):])
        res.append(word2[len(word1):])
        return "".join(res)
        