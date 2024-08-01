# Median of two sorted arrays

[Problem link](https://leetcode.com/problems/median-of-two-sorted-arrays/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution {
 public:
  using vec = vector<int>;
  int kth(vec& ar1, vec& ar2, int n1, int n2, int k) {
    // Binary search: First pos in ar1 >= kth combined element
    int k1start = 0, k1end = n1 + 1;
    while (k1end - k1start > 1) {
      int k1 = (k1start + k1end) >> 1, k2 = k - k1;
      if ((k2 < 0) or (k1 and (k2 < n2) and (ar2[k2] < ar1[k1 - 1])))
        k1end = k1;
      else
        k1start = k1;
    }

    int &k1 = k1start, k2 = k - k1;
    if (k1 == n1)
      return ar2[k2];
    else if (k2 == n2)
      return ar1[k1];
    else
      return min(ar1[k1], ar2[k2]);
  }
  double findMedianSortedArrays(vec& nums1, vec& nums2) {
    int n1 = nums1.size(), n2 = nums2.size(), n = n1 + n2;
    double ret = kth(nums1, nums2, n1, n2, n / 2);
    if (!(n & 1)) ret = (ret + kth(nums1, nums2, n1, n2, n / 2 - 1)) / 2;
    return ret;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
