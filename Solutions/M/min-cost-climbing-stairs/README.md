# Min cost climbing stairs

[Problem link](https://leetcode.com/problems/min-cost-climbing-stairs)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/min-cost-climbing-stairs

class Solution {
 public:
  int minCostClimbingStairs(vector<int>& cost) {
    for (int i = cost.size() - 3; i >= 0; --i)
      cost[i] += min(cost[i + 1], cost[i + 2]);
    return min(cost[0], cost[1]);
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
