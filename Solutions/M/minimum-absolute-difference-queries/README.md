# Minimum absolute difference queries

[Problem link](https://leetcode.com/problems/minimum-absolute-difference-queries)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-absolute-difference-queries

class Solution {
 public:
  vector<int> minDifference(vector<int>& nums, vector<vector<int>>& queries) {
    unordered_set<int> pts;
    for (auto& v : queries) {
      pts.insert(--v[0]);
      pts.insert(v[1]);
    }

    int m = *min_element(nums.begin(), nums.end()),
        M = *max_element(nums.begin(), nums.end()), X = M - m + 1,
        N = nums.size();
    vector<int> cnt(X);
    unordered_map<int, vector<int>> pref;
    if (pts.count(-1)) pref[-1] = cnt;
    for (int i = 0; i < N; ++i) {
      ++cnt[nums[i] - m];
      if (pts.count(i)) pref[i] = cnt;
    }

    vector<int> ret;
    const int INF = 1000000;
    for (auto& v : queries) {
      int best = INF;
      auto& pl = pref[v[0]];
      auto& pr = pref[v[1]];
      for (int i = 0, prev = -1; i < X; ++i) {
        if (pl[i] == pr[i]) continue;
        if (prev != -1) best = min(best, i - prev);
        prev = i;
      }
      if (best == INF) best = -1;
      ret.push_back(best);
    }
    return ret;
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
* [Offline query processing](/Collections/offline-query-processing.md#offline-query-processing)
