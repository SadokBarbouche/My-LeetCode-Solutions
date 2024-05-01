class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if not ch in word:
            return word
        rev = ""
        for i in range(len(word)):
            if word[i] == ch:
                rev = word[:i+1][::-1]
                return rev + word[i+1:]
        return ""
            