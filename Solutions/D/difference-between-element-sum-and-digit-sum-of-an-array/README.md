# Difference between element sum and digit sum of an array

[Problem link](https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

class Solution {
 public:
  int digsum(int x) {
    if (x < 10) return x;
    return x % 10 + digsum(x / 10);
  }
  int differenceOfSum(vector<int>& nums) {
    int tot{};
    for (int x : nums) tot += x - digsum(x);
    return tot;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
