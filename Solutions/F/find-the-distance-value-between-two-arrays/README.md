# Find the distance value between two arrays

[Problem link](https://leetcode.com/problems/find-the-distance-value-between-two-arrays)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-distance-value-between-two-arrays

class Solution {
 public:
  int findTheDistanceValue(vector<int>& arr1, vector<int>& arr2, int d) {
    int ret = 0;
    for (int n1 : arr1) {
      ++ret;
      for (int n2 : arr2)
        if (abs(n1 - n2) <= d) {
          --ret;
          break;
        }
    }
    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
