# Match substring after replacement

[Problem link](https://leetcode.com/problems/match-substring-after-replacement)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/match-substring-after-replacement

class Solution {
 public:
  bool matchReplacement(string s, string sub, vector<vector<char>>& mappings) {
    vector<vector<char>> cnt(256, vector<char>(256));
    for (auto v : mappings) cnt[v[1]][v[0]] = 1;
    int m = s.size(), n = sub.size();
    for (int i = 0; i + n <= m; ++i) {
      bool flag = true;
      for (int j = 0; j < n and flag; ++j) {
        char c1 = s[i + j], c2 = sub[j];
        if (c1 != c2 and !cnt[c1][c2]) flag = false;
      }
      if (flag) return true;
    }
    return false;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
