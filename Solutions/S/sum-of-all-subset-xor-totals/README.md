# Sum of all subset xor totals

[Problem link](https://leetcode.com/problems/sum-of-all-subset-xor-totals)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sum-of-all-subset-xor-totals

class Solution {
 public:
  int subsetXORSum(vector<int>& nums) {
    int ret = 0, n = nums.size();
    for (int i = 0; i < (1 << n); ++i) {
      int cur = 0;
      for (int j = 0; j < n; ++j)
        if (i & (1 << j)) cur ^= nums[j];
      ret += cur;
    }
    return ret;
  }
};
```