# Maximum sum queries

[Problem link](https://leetcode.com/problems/maximum-sum-queries/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-sum-queries/

class Solution {
 public:
  vector<int> maximumSumQueries(vector<int>& nums1, vector<int>& nums2,
                                vector<vector<int>>& queries) {
    int n = nums1.size(), q = queries.size();
    vector<int> idx(n), qidx(q), ret(q);
    iota(idx.begin(), idx.end(), 0);
    sort(idx.begin(), idx.end(),
         [&](int i, int j) { return nums1[i] > nums1[j]; });
    iota(qidx.begin(), qidx.end(), 0);
    sort(qidx.begin(), qidx.end(),
         [&](int i, int j) { return queries[i][0] > queries[j][0]; });
    map<int, int> best{{1 << 30, -1}};
    for (int i = 0, j = 0; i < q; ++i) {
      int query = qidx[i], x = queries[query][0], y = queries[query][1];
      while (j < n and nums1[idx[j]] >= x) {
        int y = nums2[idx[j]], good = y + nums1[idx[j]];
        ++j;
        auto mit = best.lower_bound(y);
        if (mit->second >= good) continue;
        mit = best.insert({y, good}).first;
        auto mit2 = mit;
        while (mit != best.begin()) {
          --mit2;
          if (mit2->second <= mit->second)
            best.erase(mit2++);
          else
            break;
        }
      }
      ret[query] = best.lower_bound(y)->second;
    }
    return ret;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Index array](/Collections/sorting.md#index-array)
* [Offline query processing](/Collections/offline-query-processing.md#offline-query-processing)
* [Binary search](/Collections/binary-search.md#binary-search) > [C++ set](/Collections/binary-search.md#c---set)
* [Stack](/Collections/stack.md#stack) > [Monotonic stack](/Collections/stack.md#monotonic-stack)
