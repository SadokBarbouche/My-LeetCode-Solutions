class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s = ["".join(sorted(s)) for s in strs]
        z = zip(strs,s)
        d = {i:[] for i in set(s)}
        for i in z:
            d[i[1]].append(i[0])
        return d.values()