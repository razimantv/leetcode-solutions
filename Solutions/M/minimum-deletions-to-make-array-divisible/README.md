# Minimum deletions to make array divisible

[Problem link](https://leetcode.com/problems/minimum-deletions-to-make-array-divisible)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-deletions-to-make-array-divisible

class Solution {
 public:
  int minOperations(vector<int>& nums, vector<int>& numsDivide) {
    sort(nums.begin(), nums.end());
    int x = accumulate(numsDivide.begin(), numsDivide.end(), numsDivide[0],
                       [](int a, int b) { return __gcd(a, b); });
    for (int i = 0, n = nums.size(); i < n; ++i)
      if (x % nums[i] == 0) return i;
    return -1;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
