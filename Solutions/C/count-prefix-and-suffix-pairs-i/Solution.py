# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        fullhashes = defaultdict(int)
        p1, mod1 = 43, 173953813
        ret = 0
        for word in words:
            l = len(word)
            fwhash1, bwhash1, p1pow = 0, 0, 1
            for i in range(l):
                fwhash1 = (
                    fwhash1 * p1 + ord(word[i]) - ord('a') + 1
                ) % mod1
                bwhash1 = (
                    bwhash1 + p1pow * (ord(word[l-1-i]) - ord('a') + 1)
                ) % mod1
                p1pow = (p1pow * p1) % mod1
                if fwhash1 == bwhash1 and fwhash1 in fullhashes:
                    ret += fullhashes[fwhash1]
            fullhashes[fwhash1] += 1
        return ret
