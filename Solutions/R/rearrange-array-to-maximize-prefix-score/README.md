# Rearrange array to maximize prefix score

[Problem link](https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/

class Solution {
 public:
  int maxScore(vector<int>& nums) {
    sort(nums.begin(), nums.end(), greater<int>());
    int ret{};
    long long pref{};
    for (int x : nums)
      if ((pref += x) > 0)
        ++ret;
      else
        break;
    return ret;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
