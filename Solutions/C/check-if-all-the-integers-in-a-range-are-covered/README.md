# Check if all the integers in a range are covered

[Problem link](https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered

class Solution {
 public:
  bool isCovered(vector<vector<int>>& ranges, int left, int right) {
    for (int i = left; i <= right; ++i) {
      bool flag = false;
      for (auto& v : ranges) {
        int l = v[0], r = v[1];
        if (l <= i and r >= i) flag = true;
      }
      if (!flag) return false;
    }
    return true;
  }
};
```
## Tags

* [Simple implementation](/README.md#Simple_implementation)
* [Suboptimal solution](/README.md#Suboptimal_solution)
