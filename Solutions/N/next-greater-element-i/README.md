# Next greater element i

[Problem link](https://leetcode.com/problems/next-greater-element-i)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/next-greater-element-i

class Solution {
 public:
  vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    int m = nums1.size(), n = nums2.size();
    nums2.push_back(-1);
    for (int i = 0; i < m; ++i) {
      int j = 0;
      while (nums2[j] != nums1[i]) ++j;
      while (j < n and nums2[j] <= nums1[i]) ++j;
      nums1[i] = nums2[j];
    }
    return nums1;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
* [Suboptimal solution](/Collections/suboptimal-solution.md#suboptimal-solution)
