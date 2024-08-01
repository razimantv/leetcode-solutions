# Longest substring with at least k repeating characters

[Problem link](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters

class Solution {
 public:
  int longestSubstring(string s, int K) {
    if (K > s.size()) return 0;
    vector<int> cnt(26);
    int bad = 0;
    for (char c : s) {
      ++cnt[c - 'a'];
      if (cnt[c - 'a'] == 1) ++bad;
      if (cnt[c - 'a'] == K) --bad;
    }
    if (bad == 0) return s.size();

    int best = 0;
    for (int i = 0, N = s.size(), l = 0;; ++i) {
      if (i == N) {
        if (l < N) best = max(best, longestSubstring(s.substr(l), K));
        break;
      }

      if (cnt[s[i] - 'a'] < K) {
        if (i - l >= K)
          best = max(best, longestSubstring(s.substr(l, i - l), K));
        l = i + 1;
      }
    }
    return best;
  }
};
```
## Tags

* [Suboptimal solution](/Collections/suboptimal-solution.md#suboptimal-solution)
