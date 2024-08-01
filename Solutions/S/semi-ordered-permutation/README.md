# Semi ordered permutation

[Problem link](https://leetcode.com/problems/semi-ordered-permutation/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/semi-ordered-permutation/

class Solution {
 public:
  int semiOrderedPermutation(vector<int>& nums) {
    int n = nums.size(), i1 = find(nums.begin(), nums.end(), 1) - nums.begin(),
        i2 = find(nums.begin(), nums.end(), n) - nums.begin();
    return i1 + n - 1 - i2 - (i1 > i2);
  }
};
```
## Tags

* [Permutation](/Collections/permutation.md#permutation) > [Swaps](/Collections/permutation.md#swaps)
