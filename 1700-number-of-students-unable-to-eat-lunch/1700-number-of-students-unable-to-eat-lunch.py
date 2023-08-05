from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        ans = 0
        for _ in range(5*n):
            if len(students) == 0:
                break
            if students[0] != sandwiches[0]:
                students.append(students.pop(0))
            else:
                students.pop(0)
                sandwiches.pop(0)
                ans += 1
        return n - ans
