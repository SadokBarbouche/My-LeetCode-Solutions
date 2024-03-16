class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_index_map = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in num_index_map:
                return [num_index_map[complement] + 1, i + 1]
            num_index_map[num] = i
        return []
