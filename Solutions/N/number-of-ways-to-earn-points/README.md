# Number of ways to earn points

[Problem link](https://leetcode.com/problems/number-of-ways-to-earn-points/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-ways-to-earn-points/

class Solution {
 public:
  int waysToReachTarget(int target, vector<vector<int>>& types) {
    vector<int> DP(target + 1);
    DP[0] = 1;

    const int MOD = 1'000'000'007;
    for (auto& q : types) {
      for (int j = target; j >= q[1]; --j)
        for (int jp = j - q[1], x = 1; jp >= 0 and x <= q[0]; jp -= q[1], ++x)
          if ((DP[j] += DP[jp]) >= MOD) DP[j] -= MOD;
    }

    return DP[target];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Knapsack](/Collections/dynamic-programming.md#knapsack)
