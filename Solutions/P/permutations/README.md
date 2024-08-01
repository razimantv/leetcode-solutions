# Permutations

[Problem link](https://leetcode.com/problems/permutations/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/permutations/

class Solution {
 public:
  vector<vector<int>> permute(vector<int>& nums) {
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

* [Brute force enumeration](/Collections/brute-force-enumeration.md#brute-force-enumeration) > [Combinatorial](/Collections/brute-force-enumeration.md#combinatorial)
