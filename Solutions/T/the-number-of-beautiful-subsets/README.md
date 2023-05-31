# The number of beautiful subsets

[Problem link](https://leetcode.com/problems/the-number-of-beautiful-subsets/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/the-number-of-beautiful-subsets/

class Solution {
 public:
  int beautifulSubsets(vector<int>& nums, int k) {
    sort(nums.begin(), nums.end());
    unordered_map<int, vector<int>> m;
    for (int x : nums) m[x % k].push_back(x);
    int ret = 1;
    for (auto& [val, vec] : m) {
      int no = 1, yes = 1;
      for (int i = 1, n = vec.size(); i < n; ++i) {
        if (vec[i] - vec[i - 1] == k) {
          int temp = no;
          no += yes;
          yes = temp;
        } else {
          yes += no;
          no = yes;
        }
      }
      ret *= (yes + no);
    }
    return ret - 1;
  }
};
```
## Tags

* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Basic](/README.md#Mathematics-Number_theory-Basic)
* [Mathematics](/README.md#Mathematics) > [Combinatorics](/README.md#Mathematics-Combinatorics)
* [Dynamic programming](/README.md#Dynamic_programming)
* [Sorting](/README.md#Sorting)
