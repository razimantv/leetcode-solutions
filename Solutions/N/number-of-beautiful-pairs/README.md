# Number of beautiful pairs

[Problem link](https://leetcode.com/problems/number-of-beautiful-pairs/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-beautiful-pairs/

class Solution {
 public:
  int countBeautifulPairs(vector<int>& nums) {
    int ret{};
    for (int i = 0, n = nums.size(); i < n; ++i) {
      int d1 = to_string(nums[i])[0] - '0';
      for (int j = i + 1; j < n; ++j)
        if (__gcd(d1, nums[j] % 10) == 1) ++ret;
    }
    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
