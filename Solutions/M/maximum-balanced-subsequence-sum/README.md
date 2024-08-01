# Maximum balanced subsequence sum

[Problem link](https://leetcode.com/problems/maximum-balanced-subsequence-sum/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-balanced-subsequence-sum/

class Solution {
 public:
  long long maxBalancedSubsequenceSum(vector<int>& nums) {
    map<long long, long long> best;
    long long ret{nums[0]};
    for (int i = 0, n = nums.size(); i < n; ++i) {
      long long x = nums[i], y = x - i, cur;
      auto mit = best.upper_bound(y);
      if (mit == best.begin()) {
        cur = best[y] = x;
      } else {
        cur = best[y] = max(0ll, (--mit)->second) + x;
      }
      ret = max(ret, cur);
      mit = best.upper_bound(y);

      while (mit != best.end() and mit->second <= cur) best.erase(mit++);
    }
    return ret;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search) > [C++ set](/Collections/binary-search.md#c---set)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Expression rearrangement](/Collections/mathematics.md#expression-rearrangement)
