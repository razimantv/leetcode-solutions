# Longest subsequence with limited sum

[Problem link](https://leetcode.com/problems/longest-subsequence-with-limited-sum/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-subsequence-with-limited-sum/

class Solution {
 public:
  vector<int> answerQueries(vector<int>& nums, vector<int>& queries) {
    sort(nums.begin(), nums.end());
    int n = nums.size();
    for (int i = 1; i < n; ++i) nums[i] += nums[i - 1];

    vector<int> ret;
    for (int q : queries) {
      ret.push_back(upper_bound(nums.begin(), nums.end(), q) - nums.begin());
    }
    return ret;
  }
};
```
## Tags

* [Greedy](/README.md#Greedy)
* [Prefix](/README.md#Prefix) > [Sum](/README.md#Prefix-Sum)
* [Binary search](/README.md#Binary_search)
