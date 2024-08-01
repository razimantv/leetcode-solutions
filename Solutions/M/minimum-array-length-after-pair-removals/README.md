# Minimum array length after pair removals

[Problem link](https://leetcode.com/problems/minimum-array-length-after-pair-removals/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-array-length-after-pair-removals/

class Solution {
 public:
  int minLengthAfterRemovals(vector<int>& nums) {
    int n = nums.size(), lmax{};
    for (int i = 0, cur = 0; i < n; ++i) {
      if (i and nums[i] != nums[i - 1]) cur = 0;
      lmax = max(lmax, ++cur);
    }
    return (2 * lmax <= n) ? (n & 1) : (2 * lmax - n);
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Hashmap](/Collections/hashmap.md#hashmap)
