class Solution:
    # Stolen code just to not break the daily
    def getCombination(self, comb:int, wheelIndex:int) -> List[int]:
        num = comb % 10**(wheelIndex+1) // 10**wheelIndex
        nextNum = comb - num * 10**wheelIndex + ((num + 1) % 10) * 10**wheelIndex
        prevNum = comb - num * 10**wheelIndex + ((num - 1 + 10) % 10) * 10**wheelIndex
        return (nextNum, prevNum,)
    
    def openLock(self, deadends: List[str], target: str) -> int:
        startCombination = 0
        target = int(target)
        totalWheels = 4
        visitedCombinations = [False] * 10**totalWheels
        for comb in deadends:
            visitedCombinations[int(comb)] = True

        if visitedCombinations[startCombination] or visitedCombinations[target]:
            return -1

        combinations = deque()
        combinations.append(startCombination)
        visitedCombinations[startCombination] = True

        steps = 0

        while combinations:
            combinationSize = len(combinations)

            for _ in range(combinationSize):
                currCombination = combinations.popleft()

                if currCombination == target:
                    return steps

                for wheelIndex in range(totalWheels):
                    nextComb, prevComb = self.getCombination(currCombination, wheelIndex)
                    if not visitedCombinations[nextComb]:
                        combinations.append(nextComb)
                        visitedCombinations[nextComb] = True
                    if not visitedCombinations[prevComb]:
                        combinations.append(prevComb)
                        visitedCombinations[prevComb] = True
            steps += 1
        return -1