class Solution:
    def frequencySort(self, s: str) -> str:
        seq2occ = dict()
        for i in s:
            if i in seq2occ:
                seq2occ[i] += 1
            else:
                seq2occ[i] = 1
        seq2occ = dict(sorted(seq2occ.items(), key=lambda item: item[1], reverse=True))
        print(seq2occ)
        ans = ""
        for i,j in seq2occ.items():
            ans += j * i
        return ans