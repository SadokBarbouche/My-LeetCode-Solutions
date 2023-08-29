class Solution:
    def bestClosingTime(self, customers: str) -> int:
        max_score = 0
        score = 0
        best_hour = -1
        for i in range(len(customers)):
            score += 1 if customers[i] == 'Y' else -1
            if score > max_score:
                max_score = score
                best_hour = i
        
        return best_hour + 1
