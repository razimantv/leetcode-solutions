# Maximum elegance of a k length subsequence

[Problem link](https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/

class Solution {
 public:
  long long findMaximumElegance(vector<vector<int>>& items, int k) {
    int n = items.size();
    vector<int> indices(n);
    iota(indices.begin(), indices.end(), 0);
    sort(indices.begin(), indices.end(),
         [&](int i, int j) { return items[i][0] > items[j][0]; });

    unordered_set<int> seen;
    long long tot{}, ret{}, cats{};
    multiset<int> lowest;
    for (int i = 0; i < n; ++i) {
      auto item = items[indices[i]];
      int p = item[0], c = item[1];
      if (i < k) {
        tot += p;
        if (!seen.count(c)) {
          ++cats;
          seen.insert(c);
        } else {
          lowest.insert(p);
        }
      } else {
        if (lowest.empty()) break;
        if (!seen.count(c)) {
          ++cats;
          seen.insert(c);
          tot += p - *lowest.begin();
          lowest.erase(lowest.begin());
        }
      }
      ret = max(ret, tot + cats * cats);
    }
    return ret;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Index array](/Collections/sorting.md#index-array)
* [Priority queue](/Collections/priority-queue.md#priority-queue) > [K smallest/largest elements](/Collections/priority-queue.md#k-smallest-largest-elements)
