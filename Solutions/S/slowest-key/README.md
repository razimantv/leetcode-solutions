# Slowest key

[Problem link](https://leetcode.com/problems/slowest-key)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/slowest-key

class Solution {
 public:
  char slowestKey(vector<int>& r, string k) {
    pair<int, char> best;
    for (int i = 0, t = 0, n = r.size(); i < n; ++i) {
      best = max(best, make_pair(r[i] - t, k[i]));
      t = r[i];
    }
    return best.second;
  }
};
```