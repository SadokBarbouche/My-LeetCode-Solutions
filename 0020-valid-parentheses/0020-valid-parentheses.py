class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets_map = {')': '(', '}': '{', ']': '['}
        
        for i in s:
            if i in brackets_map.values():
                stack.append(i)
            elif i in brackets_map.keys():
                if not stack or stack.pop() != brackets_map[i]:
                    return False
                
        return not stack
