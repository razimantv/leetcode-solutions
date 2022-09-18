// https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/

class Solution {
 public:
  int longestContinuousSubstring(string s) {
    int best = 1;
    for (int i = 1, n = s.size(), current = 1; i < n; ++i) {
      if (s[i] == s[i - 1] + 1)
        best = max(best, ++current);
      else
        current = 1;
    }
    return best;
  }
};
