# Minimum common value

[Problem link](https://leetcode.com/problems/minimum-common-value/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-common-value/

class Solution {
 public:
  int getCommon(vector<int>& nums1, vector<int>& nums2) {
    for (int i = 0, j = 0, m = nums1.size(), n = nums2.size();
         i < m and j < n;) {
      if (nums1[i] == nums2[j])
        return nums1[i];
      else if (nums1[i] < nums2[j])
        ++i;
      else
        ++j;
    }
    return -1;
  }
};
```
## Tags

* [Two pointers](/Collections/two-pointers.md#two-pointers)
