# 4sum

[Problem link](https://leetcode.com/problems/4sum)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/4sum

class Solution {
 public:
  vector<vector<int>> fourSum(vector<int>& nums, int target) {
    int n = nums.size();
    sort(nums.begin(), nums.end());
    unordered_map<int, set<pair<int, int>>> lsum;
    set<tuple<int, int, int, int>> seen;

    for (int i = 0; i < n; ++i) {
      for (int j = i + 1; j < n; ++j)
        for (auto& [a, b] : lsum[target - nums[i] - nums[j]])
          seen.insert({a, b, nums[i], nums[j]});
      for (int j = 0; j < i; ++j)
        lsum[nums[j] + nums[i]].insert({nums[j], nums[i]});
    }

    vector<vector<int>> ret;
    for (auto [a, b, c, d] : seen) ret.push_back({a, b, c, d});
    return ret;
  }
};
```
## Tags

* [Meet in the middle](/Collections/meet-in-the-middle.md#meet-in-the-middle)
