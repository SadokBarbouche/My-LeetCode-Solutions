class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        ans = []
        while count:
            most_common_tasks = count.most_common(n + 1)
            for task, freq in most_common_tasks:
                ans.append(task)
                count[task] -= 1
                if count[task] == 0:
                    del count[task]
            if not count:
                break
            while len(ans) % (n + 1) != 0:
                ans.append('idle')
        return len(ans)
