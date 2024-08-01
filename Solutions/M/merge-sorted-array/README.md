# Merge sorted array

[Problem link](https://leetcode.com/problems/merge-sorted-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/merge-sorted-array

class Solution {
 public:
  void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    for (int p = m + n - 1, i = m - 1, j = n - 1; p >= 0; --p) {
      if (i < 0)
        nums1[p] = nums2[j--];
      else if (j < 0 or nums1[i] > nums2[j])
        nums1[p] = nums1[i--];
      else
        nums1[p] = nums2[j--];
    }
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Merge sort](/Collections/sorting.md#merge-sort)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [In-place modification](/Collections/array-scanning.md#in-place-modification)
