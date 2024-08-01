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

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
* [Sorting](/Collections/sorting.md#sorting)
