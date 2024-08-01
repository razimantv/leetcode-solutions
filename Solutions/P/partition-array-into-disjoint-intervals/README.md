# Partition array into disjoint intervals

[Problem link](https://leetcode.com/problems/partition-array-into-disjoint-intervals)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/partition-array-into-disjoint-intervals

class Solution {
 public:
  int partitionDisjoint(vector<int>& nums) {
    int n = nums.size();
    vector<int> small(n);
    small[n - 1] = nums[n - 1];
    for (int i = n - 2; i >= 0; --i) small[i] = min(small[i + 1], nums[i]);

    int large = 0;
    for (int i = 0; i < n - 1; ++i) {
      large = max(large, nums[i]);
      if (large <= small[i + 1]) return i + 1;
    }
    return -1;
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Extremum](/Collections/prefix.md#extremum)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [From both ends of array](/Collections/array-scanning.md#from-both-ends-of-array)
