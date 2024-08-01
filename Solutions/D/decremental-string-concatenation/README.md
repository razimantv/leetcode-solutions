# Decremental string concatenation

[Problem link](https://leetcode.com/problems/decremental-string-concatenation/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/decremental-string-concatenation/

class Solution {
 public:
  int minimizeConcatenatedLength(vector<string>& words) {
    string empty;
    unordered_map<string, int> dp{
        {empty + words[0][0] + words[0].back(), words[0].size()}};

    for (int i = 1, n = words.size(); i < n; ++i) {
      char s = words[i][0], e = words[i].back();
      int l = words[i].size();
      unordered_map<string, int> next;
      for (auto [k, v] : dp) {
        char ss = k[0], ee = k[1];
        string se = empty + s + ee;
        if (!next.count(se)) next[se] = INT_MAX;
        next[se] = min(next[se], v + l - (e == ss));

        se = empty + ss + e;
        if (!next.count(se)) next[se] = INT_MAX;
        next[se] = min(next[se], v + l - (s == ee));
      }
      dp = next;
    }

    int ret{1234567};
    for (auto [k, v] : dp) ret = min(ret, v);
    return ret;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Partial bottom-up](/Collections/dynamic-programming.md#partial-bottom-up)
