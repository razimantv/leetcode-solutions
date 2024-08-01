# Intersection of two arrays ii

[Problem link](https://leetcode.com/problems/intersection-of-two-arrays-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution {
 public:
  vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
    vector<int> ret;
    vector<short> cnt(1001);
    for (int x : nums1) ++cnt[x];
    for (int x : nums2)
      if (cnt[x]-- > 0) ret.push_back(x);
    return ret;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Counting elements in array](/Collections/counting-elements-in-array.md#counting-elements-in-array)
