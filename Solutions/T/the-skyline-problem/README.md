# The skyline problem

[Problem link](https://leetcode.com/problems/the-skyline-problem)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/the-skyline-problem

class Solution {
 public:
  vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
    struct end {
      int x, y, t;
      bool operator<(const end& e) const { return x < e.x; }
    };

    vector<end> pts;
    for (const auto& b : buildings) {
      pts.push_back({b[0], b[2], 0});
      pts.push_back({b[1], b[2], 1});
    }
    sort(pts.begin(), pts.end());

    multiset<int, greater<int>> h{0};
    vector<vector<int>> ret;
    for (int i = 0, N = pts.size(), j = i, prev = 0; i < N; i = j) {
      for (; j < N and pts[j].x == pts[i].x; ++j) {
        if (pts[j].t == 0)
          h.insert(pts[j].y);
        else
          h.erase(h.find(pts[j].y));
      }
      if (*h.begin() != prev) {
        prev = *h.begin();
        ret.push_back({pts[i].x, prev});
      }
    }
    return ret;
  }
};
```