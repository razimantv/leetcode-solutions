# Minimum total distance traveled

[Problem link](https://leetcode.com/problems/minimum-total-distance-traveled/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-total-distance-traveled/

class Solution {
 public:
  long long minimumTotalDistance(vector<int>& robot,
                                 vector<vector<int>>& factory) {
    vector<int> factories;
    sort(factory.begin(), factory.end());
    sort(robot.begin(), robot.end());
    for (auto& f : factory) {
      int pos = f[0], cnt = f[1];
      for (int i = 0; i < cnt; ++i) factories.push_back(pos);
    }

    int F = factories.size();
    vector<long long> dp(F + 1);
    for (int r : robot) {
      vector<long long> newdp(F + 1, 1ll << 50);
      for (int i = 1; i <= F; ++i)
        newdp[i] = min(newdp[i - 1], dp[i - 1] + abs(r - factories[i - 1]));
      dp = newdp;
    }
    return dp.back();
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
