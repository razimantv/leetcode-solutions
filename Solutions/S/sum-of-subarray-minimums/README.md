# Sum of subarray minimums

[Problem link](https://leetcode.com/problems/sum-of-subarray-minimums)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sum-of-subarray-minimums

class Solution {
 public:
  int parent(int u, vector<int>& par) {
    return (u == par[u]) ? u : (par[u] = parent(par[u], par));
  }
  int sumSubarrayMins(vector<int>& arr) {
    int n = arr.size();
    vector<int> par(n, -1), left(n);
    iota(left.begin(), left.end(), 0);
    vector<int> right = left, index = left;
    sort(index.begin(), index.end(),
         [&](int a, int b) { return arr[a] > arr[b]; });
    long long ret{};
    for (int u : index) {
      par[u] = u;
      if (u > 0 and par[u - 1] != -1) {
        int v = parent(u - 1, par);
        par[v] = u;
        left[u] = left[v];
      }
      if (u < n - 1 and par[u + 1] != -1) {
        int v = parent(u + 1, par);
        par[v] = u;
        right[u] = right[v];
      }
      ret = (ret + (u - left[u] + 1) * (long long)(right[u] - u + 1) * arr[u]) %
            1'000'000'007;
    }
    return ret;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Remembering index](/Collections/sorting.md#remembering-index)
* [Disjoint set union](/Collections/disjoint-set-union.md#disjoint-set-union)
