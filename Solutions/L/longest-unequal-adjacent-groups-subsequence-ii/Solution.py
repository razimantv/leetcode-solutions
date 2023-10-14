# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        def hamming(w1, w2):
            if len(w1) != len(w2):
                return False
            ret = False
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if ret:
                        return False
                    ret = True
            return ret

        dp = [1] * n
        i0 = 0
        for i, (w, g) in enumerate(zip(words, groups)):
            for j, (wp, gp) in enumerate(zip(words[:i], groups[:i])):
                if gp != g and hamming(wp, w) and dp[j] >= dp[i]:
                    dp[i] = dp[j] + 1
            if dp[i] > dp[i0]:
                i0 = i

        ret = []
        while True:
            ret. append(words[i0])
            for i in range(i0-1, -1, -1):
                if groups[i0] != groups[i] and dp[i] == dp[i0]-1 and hamming(words[i0], words[i]):
                    i0 = i
                    break
            else:
                break
        return ret[::-1]
