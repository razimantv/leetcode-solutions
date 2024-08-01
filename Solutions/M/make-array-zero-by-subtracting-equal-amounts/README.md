# Make array zero by subtracting equal amounts

[Problem link](https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts

class Solution {
 public:
  int minimumOperations(vector<int>& nums) {
    set<int> s;
    for (int x : nums)
      if (x) s.insert(x);
    return s.size();
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
