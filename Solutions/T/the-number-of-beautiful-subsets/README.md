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
    unordered_map<int, map<int, int>> m;
    for (int x : nums) m[x % k][x] += 1;
    int ret = 1;
    for (auto& [_, vec] : m) {
      int no = 1, yes = 0, prev = -k - 1;
      for (auto [x, cnt] : vec) {
        if (x - prev == k) {
          int temp = no;
          no += yes;
          yes = (temp << cnt) - temp;
        } else {
          no += yes;
          yes = (no << cnt) - no;
        }
        prev = x;
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
