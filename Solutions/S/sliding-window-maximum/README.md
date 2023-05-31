# Sliding window maximum

[Problem link](https://leetcode.com/problems/sliding-window-maximum)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sliding-window-maximum

class Solution {
 public:
  vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    deque<pair<int, int>> cur;
    vector<int> ret;
    for (int i = 0, N = nums.size(); i < N; ++i) {
      while (!cur.empty() and cur.back().first <= nums[i]) cur.pop_back();
      cur.push_back({nums[i], i});
      if (cur.front().second <= i - k) cur.pop_front();
      if (i >= k - 1) ret.push_back(cur.front().first);
    }
    return ret;
  }
};
```