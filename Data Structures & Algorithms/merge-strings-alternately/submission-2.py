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
        # # zip use krke thoda better version
        # res = []
        # for ch1, ch2 in zip(word1, word2):
        #     res.append(ch1)
        #     res.append(ch2)
        # res.append(word1[len(word2):])
        # res.append(word2[len(word1):])
        # return "".join(res)

        # ..........................................
        # best optimal solution using two pointer
        res = []
        i,j=0,0
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i+=1
            j+=1
        # leftover elements
        while i<len(word1):
            res.append(word1[i])
            i+=1
        # rightover elements
        while j<len(word2):
            res.append(word2[j])
            j+=1
        return "".join(res)
        