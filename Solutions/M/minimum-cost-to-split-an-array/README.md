# Minimum cost to split an array

[Problem link](https://leetcode.com/problems/minimum-cost-to-split-an-array/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-cost-to-split-an-array/

class Solution {
 public:
  int minCost(vector<int>& nums, int k) {
    int n = nums.size();
    vector<int> dp(n + 1, 1'100'000'000);
    dp.back() = 0;
    for (int i = n - 1; i >= 0; --i) {
      unordered_set<int> one, more;
      for (int j = i; j < n; ++j) {
        int x = nums[j];
        if (one.count(x))
          one.erase(x), more.insert(x);
        else if (!more.count(x))
          one.insert(x);
        dp[i] = min(dp[i], dp[j + 1] + k + j - i + 1 - (int)one.size());
      }
    }
    return dp[0];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
* [Hashmap](/Collections/hashmap.md#hashmap)
