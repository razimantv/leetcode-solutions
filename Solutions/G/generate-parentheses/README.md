# Generate parentheses

[Problem link](https://leetcode.com/problems/generate-parentheses)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/generate-parentheses

class Solution {
 public:
  vector<vector<string>> ret;
  vector<string> generateParenthesis(int n) {
    ret.resize(n + 1);
    ret[0] = {""};
    for (int i = 1; i <= n; ++i)
      for (int j = 0; j < i; ++j)
        for (auto &s1 : ret[j])
          for (auto &s2 : ret[i - 1 - j]) ret[i].push_back("(" + s1 + ")" + s2);
    return ret.back();
  }
};
```
## Tags

* [Backtracking](/Collections/backtracking.md#backtracking)
