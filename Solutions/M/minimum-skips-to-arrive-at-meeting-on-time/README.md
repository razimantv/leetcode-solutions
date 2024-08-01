# Minimum skips to arrive at meeting on time

[Problem link](https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-skips-to-arrive-at-meeting-on-time

class Solution {
 public:
  int minSkips(vector<int>& dist, int speed, int hoursBefore) {
    int N = dist.size();
    vector<vector<double>> DP(2, vector<double>(N, 0));
    for (int i = 1; i < N; ++i) {
      DP[0][i] = DP[0][i - 1] + ceil(dist[i - 1] / (double)speed);
    }

    double eps = 1e-9;
    if (DP[0].back() + dist.back() / (double)speed < hoursBefore + eps)
      return 0;

    for (int i = 1; i <= N; ++i) {
      int c = i & 1, p = c ^ 1;
      for (int j = 1; j < N; ++j) {
        DP[c][j] = min(DP[p][j],
                       ceil(DP[c][j - 1] + dist[j - 1] / (double)speed - eps));
        DP[c][j] = min(DP[c][j], DP[p][j - 1] + dist[j - 1] / (double)speed);
      }
      if (DP[c].back() + dist.back() / (double)speed < hoursBefore + eps)
        return i;
    }
    return -1;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
