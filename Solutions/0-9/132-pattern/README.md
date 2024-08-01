# 132 pattern

[Problem link](https://leetcode.com/problems/132-pattern)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/132-pattern

class Solution {
 public:
  bool find132pattern(vector<int>& nums) {
    int N = nums.size();
    vector<int> left(N);

    int best = nums[0];
    for (int i = 1; i < N; ++i) {
      left[i] = best;
      best = min(best, nums[i]);
    }

    set<int> seen;
    for (int i = N - 1; i > 0; --i) {
      auto sit = seen.upper_bound(-nums[i]);
      if (sit != seen.end() and -*sit > left[i]) return true;
      seen.insert(-nums[i]);
    }
    return false;
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Extremum](/Collections/prefix.md#extremum)
* [Binary search](/Collections/binary-search.md#binary-search) > [C++ set](/Collections/binary-search.md#c---set)
