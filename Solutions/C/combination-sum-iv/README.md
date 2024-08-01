# Combination sum iv

[Problem link](https://leetcode.com/problems/combination-sum-iv)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/combination-sum-iv

class Solution {
 public:
  vector<int> cache;

  int combinationSum4(vector<int>& nums, int target) {
    if (cache.empty()) {
      cache = vector<int>(target + 1, -1);
      cache[0] = 1;
    }
    if (cache[target] != -1) return cache[target];

    cache[target] = 0;
    for (int n : nums)
      if (n <= target) cache[target] += combinationSum4(nums, target - n);
    return cache[target];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)
