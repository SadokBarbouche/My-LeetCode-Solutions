class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        counter = 0
        for i, j in zip(v1, v2):
            if int(i) > int(j):
                return 1
            elif int(i) < int(j):
                return -1
            counter += 1
        bigger = v1 if len(v1) > len(v2) else v2
        for i in bigger[counter:]:
            if int(i) != 0:
                return 1 if bigger == v1 else -1
        return 0
