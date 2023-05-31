# Shortest subarray with sum at least k

[Problem link](https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k

class Solution {
 public:
  int shortestSubarray(vector<int>& nums, int k) {
    deque<pair<long long, int>> q;
    q.push_back({0ll, 0});
    int n = nums.size(), best = n + 1;
    long long pref{};
    for (int i = 0; i < n; ++i) {
      pref += nums[i];
      while (!q.empty()) {
        auto [val, pos] = q.front();
        if (val <= pref - k) {
          best = min(best, i - pos + 1);
          q.pop_front();
        } else
          break;
      }
      while (!q.empty()) {
        auto [val, pos] = q.back();
        if (val >= pref)
          q.pop_back();
        else
          break;
      }
      q.push_back({pref, i + 1});
    }
    return best > n ? -1 : best;
  }
};
```