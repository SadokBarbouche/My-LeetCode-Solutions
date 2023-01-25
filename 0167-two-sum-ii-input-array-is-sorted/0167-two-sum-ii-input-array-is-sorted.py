class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums=numbers
        freq = {i:[] for i in nums}
        for i in range(len(nums)):
            freq[nums[i]].append(i)
        for i in range(len(nums)):
            if target-nums[i] in freq:
                ind_1 = freq[nums[i]][0]
                ind_2 = freq[target-nums[i]][0]
                if ind_1 != ind_2:
                    return [ind_1+1,ind_2+1]
                else:
                    if len(freq[nums[i]])>1:
                        ind_1 = freq[nums[i]][0]
                        ind_2 = freq[nums[i]][1]
                        return [ind_1+1,ind_2+1]
                    elif len(freq[target-nums[i]])>1:
                        ind_1 = freq[target-nums[i]][0]
                        ind_2 = freq[target-nums[i]][1]
                        return [ind_1+1,ind_2+1]
                        
        return []