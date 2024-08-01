# Minimum number of operations to make all array elements equal to 1

[Problem link](https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-number-of-operations-to-make-all-array-elements-equal-to-
class Solution {
 public:
  int minOperations(vector<int>& nums) {
    int n = nums.size();
    if (*min_element(nums.begin(), nums.end()) == 1) {
      int ret{};
      for (int x : nums) ret += x > 1;
      return ret;
    }
    for (int L = 2; L <= n; ++L) {
      for (int i = 0, j = i + L - 1; j < n; ++i, ++j) {
        int g{};
        for (int k = i; k <= j; ++k) g = __gcd(g, nums[k]);
        if (g == 1) return L + n - 2;
      }
    }
    return -1;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
* [Greedy](/Collections/greedy.md#greedy)
