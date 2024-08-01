# Painting the walls

[Problem link](https://leetcode.com/problems/painting-the-walls/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/painting-the-walls/

class Solution {
 public:
  int paintWalls(vector<int>& cost, vector<int>& time) {
    // Constraint: sum_i(time_i) >= sum_{not i} (1) = n - sum_i 1
    // => sum_i (time_i + 1) >= n
    // dp[(i,)j] = minimum cost to make paid painters paint walls
    // if they need to take at least sum(time+1) = j

    int n = cost.size();
    vector<int> dp(n + 1, 1'000'000'000);
    dp[0] = 0;
    for (int i = 0; i < n; ++i)
      for (int j = n; j >= 0; --j) {
        int target = min(j + time[i] + 1, n);
        dp[target] = min(dp[target], dp[j] + cost[i]);
        if (j < n) dp[j] = min(dp[j], dp[j + 1]);
      }
    return dp[n];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Knapsack](/Collections/dynamic-programming.md#knapsack) > [State modification](/Collections/dynamic-programming.md#state-modification)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
