# Minimum number of refueling stops

[Problem link](https://leetcode.com/problems/minimum-number-of-refueling-stops)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-number-of-refueling-stops

class Solution {
 public:
  int minRefuelStops(int target, int startFuel, vector<vector<int>>& stations) {
    if (target <= startFuel)
      return 0;
    else if (stations.empty() or startFuel < stations[0][0])
      return -1;

    int N = stations.size(), pos = 0;
    vector<long long> best(N + 1, startFuel);
    for (auto& v : stations) {
      int p = v[0], f = v[1];
      for (int i = N; i >= 0; --i) {
        best[i] -= p - pos;
        if (i and best[i - 1] >= p - pos)
          best[i] = max(best[i], best[i - 1] - (p - pos) + f);
      }
      pos = p;
    }
    for (int i = 0; i <= N; ++i)
      if (best[i] >= target - pos) return i;
    return -1;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
