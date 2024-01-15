class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win_count = {}
        loss_count = {}
        
        for match in matches:
            winner, loser = match
            win_count[winner] = win_count.get(winner, 0) + 1
            loss_count[loser] = loss_count.get(loser, 0) + 1
            if loser not in win_count:
                win_count[loser] = 0
        
        always_winners = [player for player in win_count if loss_count.get(player, 0) == 0]
        losers_once = [player for player in loss_count if loss_count[player] == 1]
        
        return [sorted(always_winners), sorted(losers_once)]
