# Minimum window substring

[Problem link](https://leetcode.com/problems/minimum-window-substring)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-window-substring

class Solution {
 public:
  bool good(const vector<int> &v) {
    for (int x : v)
      if (x > 0) return false;
    return true;
  }
  string minWindow(string s, string t) {
    vector<int> cnt(58);

    for (char c : t) ++cnt[c - 'A'];
    int best = 0, besti = 0;
    for (int i = 0, j = 0; s[i]; ++i) {
      while (s[j] and !good(cnt)) --cnt[s[j++] - 'A'];
      if (!good(cnt)) break;
      if (best == 0 or j - i < best) best = j - i, besti = i;
      ++cnt[s[i] - 'A'];
    }
    return s.substr(besti, best);
  }
};
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
