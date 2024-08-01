# Points that intersect with cars

[Problem link](https://leetcode.com/problems/points-that-intersect-with-cars/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/points-that-intersect-with-cars/

class Solution {
 public:
  int numberOfPoints(vector<vector<int>>& nums) {
    vector<int> hascar(101);
    for (auto car : nums)
      for (int i = car[0]; i <= car[1]; ++i) hascar[i] = 1;
    return accumulate(hascar.begin(), hascar.end(), 0);
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
