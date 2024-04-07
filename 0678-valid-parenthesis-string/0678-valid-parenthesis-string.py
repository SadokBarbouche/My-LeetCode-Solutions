class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        stars = []
        for i, char in enumerate(s):
            if char == '*':
                stars.append(i)
            elif char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    if stars:
                        stars.pop()
                    else:
                        return False
        while stars and stack:
            if stars[-1] < stack[-1]:
                return False
            stack.pop();stars.pop()
        
        return not stack
