class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        extended_intervals = [(start, end) for start, end in intervals] + [(newInterval[0], newInterval[1])]
        # print(extended_intervals)
        extended_intervals.sort(key=lambda x: x[0])
        # print(extended_intervals)
        merged_intervals = []
        for start, end in extended_intervals:
            if not merged_intervals or merged_intervals[-1][1] < start:
                merged_intervals.append([start, end])
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], end)
        return merged_intervals
