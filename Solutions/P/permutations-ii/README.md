# Permutations ii

[Problem link](https://leetcode.com/problems/permutations-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/permutations-ii

class Solution {
 public:
  vector<vector<int>> permuteUnique(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    vector<vector<int>> ret;
    do {
      ret.push_back(nums);
    } while (next_permutation(nums.begin(), nums.end()));
    return ret;
  }
};
```
## Tags

* [Permutation](/README.md#Permutation) > [Next/Previous](/README.md#Permutation-Next_Previous)
