# Find the maximum divisibility score

[Problem link](https://leetcode.com/problems/find-the-maximum-divisibility-score/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-maximum-divisibility-score/

class Solution {
 public:
  int maxDivScore(vector<int>& nums, vector<int>& divisors) {
    int best, val{-1};
    sort(divisors.begin(), divisors.end());
    for (int x : divisors) {
      int cnt{};
      for (int y : nums)
        if (y % x == 0) ++cnt;
      if (cnt > val) val = cnt, best = x;
    }
    return best;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
