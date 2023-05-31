# Top k frequent elements

[Problem link](https://leetcode.com/problems/top-k-frequent-elements)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/top-k-frequent-elements

class Solution {
 public:
  vector<int> topKFrequent(vector<int>& nums, int k) {
    unordered_map<int, int> cnt;
    vector<vector<int>> inv(nums.size() + 1);
    for (int n : nums) cnt[n]++;

    for (auto p : cnt) {
      inv[p.second].push_back(p.first);
    }

    vector<int> ret;
    for (int i = nums.size(); k; --i) {
      for (int n : inv[i]) ret.push_back(n), --k;
    }
    return ret;
  }
};
```