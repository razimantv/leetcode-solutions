# Container with most water

[Problem link](https://leetcode.com/problems/container-with-most-water)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/container-with-most-water

class Solution {
 public:
  int maxArea(vector<int>& height) {
    int n = height.size();
    vector<pair<int, int>> vec(n);
    for (int i = 0; i < n; ++i) vec[i] = {height[i], i};
    sort(vec.begin(), vec.end(), greater<pair<int, int>>());

    int best = 0, l = vec[0].second, r = l;
    for (int i = 0; i < n; ++i) {
      auto [h, pos] = vec[i];
      l = min(l, pos);
      r = max(r, pos);
      best = max(best, h * (r - l));
    }
    return best;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Custom](/Collections/sorting.md#custom)
