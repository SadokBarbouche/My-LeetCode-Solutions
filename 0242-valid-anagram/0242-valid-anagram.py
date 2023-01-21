class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_to_list = [i for i in s]
        t_to_list = [i for i in t]
        s_to_list.sort()
        t_to_list.sort()
        return s_to_list == t_to_list
        