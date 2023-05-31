# Shortest unsorted continuous subarray

[Problem link](https://leetcode.com/problems/shortest-unsorted-continuous-subarray)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/shortest-unsorted-continuous-subarray

class Solution {
 public:
  int findUnsortedSubarray(vector<int>& nums) {
    auto nums2 = nums;
    sort(nums2.begin(), nums2.end());

    if (nums == nums2) return 0;

    int n = nums.size(), ret = n;
    for (int i = 0; nums[i] == nums2[i]; ++i) --ret;
    for (int i = n - 1; nums[i] == nums2[i]; --i) --ret;
    return ret;
  }
};
```