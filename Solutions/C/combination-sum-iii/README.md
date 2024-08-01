# Combination sum iii

[Problem link](https://leetcode.com/problems/combination-sum-iii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/combination-sum-iii

class Solution {
  map<tuple<int, int, int>, vector<vector<int>>> memo;

 public:
  vector<vector<int>> combinationSum3(int k, int n, int last = 9) {
    if (k * (k + 1) > 2 * n or k * (2 * last - k + 1) < 2 * n)
      return {};
    else if (k == 1)
      return vector<vector<int>>(1, vector<int>(1, n));
    else if (memo.count({k, n, last}))
      return memo[{k, n, last}];

    vector<vector<int>> ret;
    for (int next = 1; next <= last; ++next) {
      auto prev = combinationSum3(k - 1, n - next, next - 1);
      for (auto& v : prev) {
        ret.push_back(v);
        ret.back().push_back(next);
      }
    }
    return memo[{k, n, last}] = ret;
  }
};
```
## Tags

* [Backtracking](/Collections/backtracking.md#backtracking)
