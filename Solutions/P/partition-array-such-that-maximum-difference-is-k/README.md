# Partition array such that maximum difference is k

[Problem link](https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k

class Solution {
 public:
  int partitionArray(vector<int>& nums, int k) {
    sort(nums.begin(), nums.end());
    int ret = 0, n = nums.size();
    for (int i = 0; i < n;) {
      ++ret;
      i = upper_bound(nums.begin() + i, nums.end(), nums[i] + k) - nums.begin();
    }
    return ret;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
