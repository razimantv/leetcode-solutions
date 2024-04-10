# https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        def work(deck):
            n = len(deck)
            if n < 3:
                return deck
            odd, even = deck[:(n+1)//2], work(deck[(n+1)//2:])
            if n % 2:
                even = even[-1:] + even[:-1]
            deck[::2] = odd
            deck[1::2] = even
            return deck

        return work(sorted(deck))
