# Sum of squares of special elements

[Problem link](https://leetcode.com/problems/sum-of-squares-of-special-elements/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sum-of-squares-of-special-elements/

class Solution {
 public:
  int sumOfSquares(vector<int>& nums) {
    int ret{};
    for (int n = nums.size(), i = 0; i < n; ++i)
      if (n % (i + 1) == 0) ret += nums[i] * nums[i];
    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
