# Two sum

[Problem link](https://leetcode.com/problems/two-sum)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/two-sum

class Solution {
 public:
  vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> seen;
    for (int i = 0, n = nums.size(); i < n; ++i) {
      if (seen.count(target - nums[i])) return {seen[target - nums[i]], i};
      seen[nums[i]] = i;
    }
    return {0, 1};
  }
};
```