class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_duration = releaseTimes[0]
        max_duration_keys = [keysPressed[0]]
        for i in range(1, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            if duration > max_duration:
                max_duration = duration
                max_duration_keys = [keysPressed[i]]
            elif duration == max_duration:
                max_duration_keys.append(keysPressed[i])
        return max(max_duration_keys)
