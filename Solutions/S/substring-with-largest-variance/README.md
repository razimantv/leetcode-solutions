# Substring with largest variance

[Problem link](https://leetcode.com/problems/substring-with-largest-variance/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/substring-with-largest-variance/

class Solution {
 public:
  int largestVariance(string s) {
    int n = s.size();
    vector<vector<int>> last(n);
    vector<int> cur(26, -1);
    unordered_set<int> seen;
    for (int i = 0; i < n; ++i) {
      cur[s[i] - 'a'] = i;
      seen.insert(s[i] - 'a');
      last[i] = cur;
    }

    int best{};
    vector<int> small(n);
    for (int c1 : seen)
      for (int c2 : seen) {
        if (c1 == c2) continue;
        for (int i = 0, diff = 0; i < n; ++i) {
          if (i) small[i] = min(small[i - 1], diff);
          if (last[i][c1] == i)
            ++diff;
          else if (last[i][c2] == i)
            --diff;
          int pos = min(last[i][c1], last[i][c2]);
          if (pos == -1) continue;
          best = max(best, diff - small[pos]);
        }
      }
    return best;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Location of previous element with same value](/Collections/array-scanning.md#location-of-previous-element-with-same-value)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
