# Longest non decreasing subarray from two arrays

[Problem link](https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/

class Solution {
 public:
  int maxNonDecreasingLength(vector<int>& nums1, vector<int>& nums2) {
    int n = nums1.size(), best{1};
    for (int i = 0, l1 = 1, l2 = 1; i < n; ++i) {
      if (nums1[i] > nums2[i]) swap(nums1[i], nums2[i]);
      if (!i) continue;
      int newl1 = 1, newl2 = 1;
      if (nums2[i] >= nums2[i - 1])
        newl2 = max(newl2, l2 + 1);
      else if (nums2[i] >= nums1[i - 1])
        newl2 = max(newl2, l1 + 1);
      if (nums1[i] >= nums2[i - 1])
        newl1 = max(newl1, l2 + 1);
      else if (nums1[i] >= nums1[i - 1])
        newl1 = max(newl1, l1 + 1);
      best = max(best, newl2);
      l1 = newl1, l2 = newl2;
    }
    return best;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Contiguous region](/Collections/array-scanning.md#contiguous-region)
