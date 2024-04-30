class Solution():
    def wonderfulSubstrings(self, word):
        count = [0] * 1024
        count[0] = 1
        ans = 0
        cur = 0
        for char in word:
            cur ^= 1 << (ord(char) - ord('a'))
            ans += count[cur]
            for i in range(10):
                new_bitmask = cur ^ (1 << i)
                if count[new_bitmask] > 0:
                    ans += count[new_bitmask]
            count[cur] += 1
        return ans 