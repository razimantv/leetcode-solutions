# Special permutations

[Problem link](https://leetcode.com/problems/special-permutations/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/special-permutations/

class Solution {
 public:
  int specialPerm(vector<int>& nums) {
    int n = nums.size(), maskcnt = 1 << n;
    const int MOD = 1'000'000'007;
    auto inc = [&](int& x, int y) {
      x += y;
      if (x >= MOD) x -= MOD;
    };

    vector<vector<int>> cnt(maskcnt, vector<int>(n));
    queue<pair<int, int>> bfsq;
    for (int i = 0; i < n; ++i) {
      cnt[1 << i][i] = 1;
      bfsq.push({1 << i, i});
    }

    while (!bfsq.empty()) {
      auto [mask, i] = bfsq.front();
      bfsq.pop();

      for (int j = 0; j < n; ++j) {
        if (mask & (1 << j)) continue;
        if (nums[i] % nums[j] == 0 or nums[j] % nums[i] == 0) {
          int newmask = mask | (1 << j);
          if (!cnt[newmask][j]) bfsq.push({newmask, j});
          inc(cnt[newmask][j], cnt[mask][i]);
        }
      }
    }

    return accumulate(cnt.back().begin(), cnt.back().end(), 0ll) % MOD;
  }
};
```
## Tags

* [Dynamic programming](/README.md#Dynamic_programming) > [Graph-like state transitions](/README.md#Dynamic_programming-Graph_like_state_transitions)
* [Dynamic programming](/README.md#Dynamic_programming) > [Subsets](/README.md#Dynamic_programming-Subsets)
* [Graph theory](/README.md#Graph_theory) > [Breadth first search](/README.md#Graph_theory-Breadth_first_search)
* [Bitwise operation](/README.md#Bitwise_operation)
