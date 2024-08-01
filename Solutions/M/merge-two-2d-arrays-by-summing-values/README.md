# Merge two 2d arrays by summing values

[Problem link](https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

class Solution {
 public:
  vector<vector<int>> mergeArrays(vector<vector<int>>& nums1,
                                  vector<vector<int>>& nums2) {
    int n1 = nums1.size(), n2 = nums2.size();
    vector<vector<int>> ret;
    auto work = [&](const vector<int>& v) {
      if (ret.empty() or ret.back()[0] < v[0])
        ret.push_back(v);
      else
        ret.back()[1] += v[1];
    };
    for (int i1 = 0, i2 = 0; i1 < n1 or i2 < n2;) {
      if (i1 == n1)
        work(nums2[i2++]);
      else if (i2 == n2)
        work(nums1[i1++]);
      else if (nums1[i1][0] < nums2[i2][0])
        work(nums1[i1++]);
      else
        work(nums2[i2++]);
    }
    return ret;
  }
};
```
## Tags

* [Two pointers](/Collections/two-pointers.md#two-pointers)
