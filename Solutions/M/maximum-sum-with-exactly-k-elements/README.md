# Maximum sum with exactly k elements

[Problem link](https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

class Solution {
 public:
  int maximizeSum(vector<int>& nums, int k) {
    int x = *max_element(nums.begin(), nums.end());
    return k * (2 * x + k - 1) / 2;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Closed form expressions](/Collections/mathematics.md#closed-form-expressions)
