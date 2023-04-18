class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        for i in zip(word1,word2):
            ans.extend(i)
        if len(word2)>len(word1):
            word1,word2 = word2,word1
        for j in range(len(ans)//2,len(word1)):
            ans.extend(word1[j])
        return "".join(ans)
            