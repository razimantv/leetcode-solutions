# Count subarrays with fixed bounds

[Problem link](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution {
 public:
  long long countSubarrays(vector<int>& nums, int minK, int maxK) {
    int n = nums.size();
    long long ret{};
    for (int i = 0, mg = -1, mb = -1, Mg = -1, Mb = -1; i < n; ++i) {
      int x = nums[i];
      if (x == minK)
        mg = i;
      else if (x < minK)
        mb = i;
      if (x == maxK)
        Mg = i;
      else if (x > maxK)
        Mb = i;
      if (min(mg, Mg) < max(mb, Mb)) continue;
      ret += min(mg, Mg) - max(mb, Mb);
    }
    return ret;
  }
};
```
## Tags

* [Prefix](/README.md#Prefix) > [Extremum](/README.md#Prefix-Extremum)
* [Valid subarray counting](/README.md#Valid_subarray_counting) > [Iterate one endpoint and keep valid range for other](/README.md#Valid_subarray_counting-Iterate_one_endpoint_and_keep_valid_range_for_other)
