# Number of subarrays with gcd equal to k

[Problem link](https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/

class Solution {
 public:
  int subarrayGCD(vector<int>& nums, int k) {
    int n = nums.size(), ret{};
    for (int i = 0; i < n; ++i) {
      for (int j = i, g = nums[i]; j < n and g >= k; ++j) {
        g = __gcd(g, nums[j]);
        if (g == k) ++ret;
      }
    }
    return ret;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
