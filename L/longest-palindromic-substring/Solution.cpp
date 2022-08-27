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
