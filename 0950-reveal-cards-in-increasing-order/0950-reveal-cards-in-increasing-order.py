class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        ans = [0] * n
        indices = deque(range(n))
        for card in deck:
            idx = indices.popleft()
            ans[idx] = card
            if indices:
                indices.append(indices.popleft())
        return ans