# Rectangle area ii

[Problem link](https://leetcode.com/problems/rectangle-area-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/rectangle-area-ii

class Solution {
 public:
  int rectangleArea(vector<vector<int>>& rectangles) {
    set<int> x, y;
    for (auto& r : rectangles) {
      x.insert(r[0]);
      x.insert(r[2]);
      y.insert(r[1]);
      y.insert(r[3]);
    }

    set<tuple<int, int, int, int>> subrect;
    for (auto& r : rectangles) {
      auto xs = x.find(r[0]), ys = y.find(r[1]);
      int x, prevx, y, prevy;
      for (auto xit = xs;; ++xit) {
        x = *xit;
        for (auto yit = ys;; ++yit) {
          y = *yit;
          if (xit != xs and yit != ys) subrect.insert({prevx, x, prevy, y});
          if ((prevy = y) == r[3]) break;
        }
        if ((prevx = x) == r[2]) break;
        ;
      }
    }

    int tot = 0;
    for (auto [x1, x2, y1, y2] : subrect)
      tot = (tot + (x2 - x1) * (long long)(y2 - y1)) % 1'000'000'007;
    return tot;
  }
};
```
## Tags

* [Intervals](/Collections/intervals.md#intervals) > [Endpoint sorting](/Collections/intervals.md#endpoint-sorting)
* [Intervals](/Collections/intervals.md#intervals) > [Non-overlapping decomposition](/Collections/intervals.md#non-overlapping-decomposition)
* [Intervals](/Collections/intervals.md#intervals) > [2D](/Collections/intervals.md#2d)
