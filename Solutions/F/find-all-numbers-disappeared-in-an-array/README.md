# Find all numbers disappeared in an array

[Problem link](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

class Solution {
 public:
  vector<int> findDisappearedNumbers(vector<int>& nums) {
    unordered_set<int> s;
    for (int x : nums) s.insert(x);

    vector<int> ret;
    for (int i = 1, n = nums.size(); i <= n; ++i)
      if (!s.count(i)) ret.push_back(i);
    return ret;
  }
};
```
## Tags

* [Unique/duplicate element finding with bizarro algorithms](/Collections/unique-duplicate-element-finding-with-bizarro-algorithms.md#unique-duplicate-element-finding-with-bizarro-algorithms)
* [Suboptimal solution](/Collections/suboptimal-solution.md#suboptimal-solution)
