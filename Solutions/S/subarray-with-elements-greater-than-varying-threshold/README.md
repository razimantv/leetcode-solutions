# Subarray with elements greater than varying threshold

[Problem link](https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold

class Solution {
 public:
  vector<int> par, left, right;

  int parent(int u) { return (par[u] == u) ? u : (par[u] = parent(par[u])); }
  int validSubarraySize(vector<int>& nums, int threshold) {
    int n = nums.size();
    vector<pair<int, int>> vp;
    for (int i = 0; i < n; ++i) vp.push_back({nums[i], i});
    sort(vp.begin(), vp.end(), greater<pair<int, int>>());

    par = left = right = vector<int>(n, -1);

    for (int i = 0, j = 1; j <= n; ++j) {
      while (i < n and vp[i].first * (long long)j > threshold) {
        int p = vp[i++].second;
        par[p] = left[p] = right[p] = p;
        if (p and par[p - 1] != -1) {
          int u = parent(p - 1);
          par[u] = p;
          left[p] = left[u];
        }
        if (p < n - 1 and par[p + 1] != -1) {
          int u = parent(p + 1);
          par[u] = p;
          right[p] = right[u];
        }

        if (right[p] - left[p] + 1 >= j) return j;
      }
    }
    return -1;
  }
};
```