class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def digitToLetters(digit):
            letters = []
            if digit <= 6:
                for i in range(3):
                    letters.append(chr(ord('a')+3*(digit-2)+i)) 
            if digit == 7:
                letters = ['p','q','r','s']
            elif digit == 8:
                letters = ['t','u','v']
            elif digit == 9:
                letters = ['w','x','y','z']
            return letters
        
        ans = []
        possibilities = []
        
        def dfs(index,letters):
            if index >= len(letters):
                ans.append("".join(possibilities[:]))
                return
            for letter in letters[index]:
                possibilities.append(letter)
                dfs(index+1,letters)
                possibilities.pop()

            
        if digits == "":
            return []
        letters = []
        for i in digits:
            letters.append(digitToLetters(int(i)))
        dfs(0,letters)
        return ans 
