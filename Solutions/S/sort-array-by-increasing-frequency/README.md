# Sort array by increasing frequency

[Problem link](https://leetcode.com/problems/sort-array-by-increasing-frequency)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sort-array-by-increasing-frequency

class Solution {
 public:
  vector<int> frequencySort(vector<int>& nums) {
    unordered_map<int, int> cnt;
    for (int n : nums) ++cnt[n];
    auto cmp = [&](int a, int b) {
      if (cnt[a] != cnt[b]) return cnt[a] < cnt[b];
      return a > b;
    };
    sort(nums.begin(), nums.end(), cmp);
    return nums;
  }
};
```