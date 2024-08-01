# Longest palindromic substring

[Problem link](https://leetcode.com/problems/longest-palindromic-substring)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-palindromic-substring

class Solution {
 public:
  string longestPalindrome(string s) {
    int best = 0, bestl = -1, n = s.size();
    for (int i = 0; i < n; ++i) {
      for (int j = i, k = i; j >= 0 && k < n; --j, ++k) {
        if (s[j] == s[k]) {
          if (k - j + 1 > best) best = k - j + 1, bestl = j;
        } else
          break;
      }
    }
    for (int i = 0; i < n; ++i) {
      for (int j = i, k = i + 1; j >= 0 && k < n; --j, ++k) {
        if (s[j] == s[k]) {
          if (k - j + 1 > best) best = k - j + 1, bestl = j;
        } else
          break;
      }
    }
    return s.substr(bestl, best);
  }
};
```
### Solution.py
```py
# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        fwhash1, bwhash1, p1pow = [0] * (n + 1), [0] * (n + 1), [1] * (n + 1)
        p1, mod1 = 43, 172510953
        for i, c in enumerate(s):
            xc = ord(c) - ord('a')
            fwhash1[i + 1] = (fwhash1[i] * p1 + xc) % mod1
            bwhash1[i + 1] = (bwhash1[i] + p1pow[i] * xc) % mod1
            p1pow[i + 1] = (p1pow[i] * p1) % mod1

        palstart, palend = 0, 0
        for centre in range(2 * n - 1):
            lc, rc = centre // 2, (centre + 1) // 2
            start, end = max(-1, centre - n), lc + 1
            while end - start > 1:
                mid = (end + start) // 2
                l, r = mid, centre - mid
                fwcur = (
                    fwhash1[r + 1] + mod1 -
                    (fwhash1[l] * p1pow[r - l + 1]) % mod1
                ) % mod1
                bwcur = (bwhash1[r + 1] + mod1 - bwhash1[l]) % mod1
                if (fwcur * p1pow[l]) % mod1 == bwcur:
                    end = mid
                else:
                    start = mid
            if centre - 2 * end > palend - palstart:
                palstart, palend = end, centre - end
        return s[palstart:palend+1]
```
## Tags

* [Palindrome](/Collections/palindrome.md#palindrome) > [Hashing](/Collections/palindrome.md#hashing)
* [Binary search](/Collections/binary-search.md#binary-search)
