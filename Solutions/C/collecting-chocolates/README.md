# Collecting chocolates

[Problem link](https://leetcode.com/problems/collecting-chocolates/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/collecting-chocolates/

class Solution {
 public:
  long long minCost(vector<int>& nums, long long x) {
    long long ret(1ll << 62);
    int n = nums.size();
    vector<long long> best(n);
    for (int i = 0; i < n; ++i) best[i] = x * i;
    for (int i = 0; i < n; ++i) {
      for (int j = 0, k = i, good = nums[i]; j < n; ++j, ++k) {
        if (k == n) k = 0;
        best[j] += (good = min(good, nums[k]));
      }
    }
    return *min_element(best.begin(), best.end());
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Cyclic array](/Collections/dynamic-programming.md#cyclic-array)
