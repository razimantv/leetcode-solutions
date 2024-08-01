# Missing number

[Problem link](https://leetcode.com/problems/missing-number)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/missing-number

class Solution {
 public:
  int missingNumber(vector<int>& nums) {
    int ret = 0;
    for (int x : nums) ret ^= x;
    for (int i = 1, n = nums.size(); i <= n; ++i) ret ^= i;
    return ret;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Unique/duplicate element finding with bizarro algorithms](/Collections/unique-duplicate-element-finding-with-bizarro-algorithms.md#unique-duplicate-element-finding-with-bizarro-algorithms)
