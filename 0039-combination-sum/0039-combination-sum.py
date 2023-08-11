class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        def dfs(index,candidates,target):
            if target == 0:
                ans.append(path.copy())
                return 
            if target < 0 or index == len(candidates):
                return
            path.append(candidates[index])            
            dfs(index,candidates,target - candidates[index])
            path.pop()
            dfs(index+1,candidates,target)
        dfs(0,candidates,target)
        return ans