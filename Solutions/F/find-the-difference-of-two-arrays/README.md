# Find the difference of two arrays

[Problem link](https://leetcode.com/problems/find-the-difference-of-two-arrays/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-difference-of-two-arrays/

class Solution {
 public:
  vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
    unordered_set<int> s1(nums1.begin(), nums1.end()),
        s2(nums2.begin(), nums2.end());
    vector<vector<int>> ret(2);
    for (int x : s1)
      if (!s2.count(x)) ret[0].push_back(x);
    for (int x : s2)
      if (!s1.count(x)) ret[1].push_back(x);
    return ret;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
