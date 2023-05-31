# Replace elements in an array

[Problem link](https://leetcode.com/problems/replace-elements-in-an-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/replace-elements-in-an-array

class Solution {
 public:
  vector<int> arrayChange(vector<int>& nums, vector<vector<int>>& operations) {
    unordered_map<int, vector<int>> pos;
    int n = nums.size();
    for (int i = 0; i < n; ++i) pos[nums[i]].push_back(i);
    for (auto op : operations) {
      int u = op[0], v = op[1];
      for (int x : pos[u]) pos[v].push_back(x);
      pos[u].clear();
    }

    for (auto [v, vec] : pos)
      for (int x : vec) nums[x] = v;
    return nums;
  }
};
```