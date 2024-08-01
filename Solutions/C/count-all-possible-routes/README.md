# Count all possible routes

[Problem link](https://leetcode.com/problems/count-all-possible-routes/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-all-possible-routes/

class Solution {
 public:
  int countRoutes(vector<int>& locations, int start, int finish, int fuel) {
    int n = locations.size();
    vector<vector<int>> cnt(fuel + 1, vector<int>(n));
    cnt[fuel][start] = 1;
    const int MOD = 1'000'000'007;
    auto inc = [&](int& x, int y) {
      x += y;
      if (x >= MOD) x -= MOD;
    };

    int ret{};
    for (int f = fuel; f >= 0; --f) {
      inc(ret, cnt[f][finish]);
      for (int i = 0; i < n; ++i) {
        if (!cnt[f][i]) continue;
        for (int j = 0, k; j < n; ++j) {
          if (i == j or (k = abs(locations[i] - locations[j])) > f) continue;
          inc(cnt[f - k][j], cnt[f][i]);
        }
      }
    }
    return ret;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Knapsack](/Collections/dynamic-programming.md#knapsack)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
