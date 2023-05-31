# Trapping rain water ii

[Problem link](https://leetcode.com/problems/trapping-rain-water-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/trapping-rain-water-ii

class Solution {
 public:
  int pairtoint(int i, int j) { return ((i + 1) << 8) | (j + 1); }

  pair<int, int> inttopair(int x) { return {(x >> 8) - 1, (x & 255) - 1}; }

  int trapRainWater(vector<vector<int>>& h) {
    int m = h.size(), n = h[0].size();
    typedef pair<int, int> cell;
    vector<int> minmax(1 << 16, -1);
    auto cmp = [&](int c1, int c2) {
      if (minmax[c1] != minmax[c2]) return minmax[c1] < minmax[c2];
      return c1 < c2;
    };
    set<int, decltype(cmp)> djset(cmp);
    for (int i = 0; i < m; ++i) {
      djset.insert(pairtoint(i, -1));
      djset.insert(pairtoint(i, n));
    }
    for (int j = 0; j < n; ++j) {
      djset.insert(pairtoint(-1, j));
      djset.insert(pairtoint(m, j));
    }

    int ret = 0;
    vector<cell> neigh{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    while (!djset.empty()) {
      int c = *djset.begin();
      auto [i, j] = inttopair(c);
      djset.erase(djset.begin());
      if (i >= 0 and i < m and j >= 0 and j < n) ret += minmax[c] - h[i][j];

      for (auto [di, dj] : neigh) {
        int ii = i + di, jj = j + dj;
        int cc;
        if (ii >= 0 and ii < m and jj >= 0 and jj < n and
            (minmax[cc = pairtoint(ii, jj)] == -1 or
             minmax[cc] > max(h[ii][jj], minmax[c]))) {
          if (minmax[cc] == -1) djset.erase(cc);
          minmax[cc] = max(minmax[c], h[ii][jj]);
          djset.insert(cc);
        }
      }
      minmax[c] = -2;
    }
    return ret;
  }
};
```