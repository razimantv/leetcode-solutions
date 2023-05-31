# Trapping rain water

[Problem link](https://leetcode.com/problems/trapping-rain-water)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/trapping-rain-water

class Solution {
 public:
  int trap(vector<int>& height) {
    if (height.empty()) return 0;
    int n = height.size();
    vector<int> left(n);
    left[0] = height[0];
    for (int i = 1; i < n; ++i) left[i] = max(height[i], left[i - 1]);

    int ret = 0;
    for (int i = n - 1, right = 0; i >= 0; --i) {
      right = max(right, height[i]);
      ret += min(left[i], right) - height[i];
    }
    return ret;
  }
};
```