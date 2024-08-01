# Maximum segment sum after removals

[Problem link](https://leetcode.com/problems/maximum-segment-sum-after-removals)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-segment-sum-after-removals

class Solution {
 public:
  vector<int> par;
  int parent(int u) { return par[u] == u ? u : (par[u] = parent(par[u])); }

  vector<long long> maximumSegmentSum(vector<int>& nums,
                                      vector<int>& removeQueries) {
    int n = nums.size();
    par = vector<int>(n, -1);

    long long best = 0;
    vector<long long> ret(n), cur(n);
    for (int j = n - 1; j; --j) {
      int i = removeQueries[j];
      par[i] = i;
      cur[i] = nums[i];
      if (i and par[i - 1] != -1) {
        int u = parent(i - 1);
        par[u] = i;
        cur[i] += cur[u];
      }
      if (i < n - 1 and par[i + 1] != -1) {
        int u = parent(i + 1);
        par[u] = i;
        cur[i] += cur[u];
      }
      ret[j - 1] = best = max(best, cur[i]);
    }
    return ret;
  }
};
```
## Tags

* [Disjoint set union](/Collections/disjoint-set-union.md#disjoint-set-union)
* [Time reversed simulation](/Collections/time-reversed-simulation.md#time-reversed-simulation)
