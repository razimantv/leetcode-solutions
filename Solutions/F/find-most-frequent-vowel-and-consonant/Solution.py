# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = 'aeiou'
        return max(
            Counter(c for c in s if c in vowels). values(), default=0
        ) + max(
            Counter(c for c in s if c not in vowels). values(), default=0
        )
