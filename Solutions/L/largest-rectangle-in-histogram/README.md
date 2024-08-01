# Largest rectangle in histogram

[Problem link](https://leetcode.com/problems/largest-rectangle-in-histogram)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/largest-rectangle-in-histogram

class Solution {
 public:
  int largestRectangleArea(vector<int>& h) {
    h.push_back(0);
    vector<pair<int, int>> s{{0, -1}};
    int n = h.size(), best = 0;
    for (int i = 0; i < n; ++i) {
      int cur = i;
      while (s.back().first > h[i]) {
        cur = s.back().second;
        best = max(best, s.back().first * (i - cur));
        s.pop_back();
      }
      s.push_back({h[i], cur});
    }
    return best;
  }
};
```
## Tags

* [Stack](/Collections/stack.md#stack) > [Monotonic stack](/Collections/stack.md#monotonic-stack)
