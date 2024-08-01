# Minimum replacements to sort the array

[Problem link](https://leetcode.com/problems/minimum-replacements-to-sort-the-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-replacements-to-sort-the-array

class Solution {
 public:
  long long minimumReplacement(vector<int>& nums) {
    long long ret = 0;
    for (int i = nums.size() - 2; i >= 0; --i) {
      int &x = nums[i], &y = nums[i + 1], add = (x - 1) / y;
      ret += add;
      x = x / (add + 1);
    }
    return ret;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Right to left](/Collections/array-scanning.md#right-to-left)
