# Find k pairs with smallest sums

[Problem link](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

class Solution {
 public:
  vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2,
                                     int k) {
    int n1 = nums1.size(), n2 = nums2.size();
    using index = pair<int, int>;
    auto val = [&](index i) { return nums1[i.first] + nums2[i.second]; };
    auto cmp = [&](index i, index j) {
      int s1 = val(i), s2 = val(j);
      return (s1 != s2) ? (s1 < s2) : (i < j);
    };

    set<index, decltype(cmp)> indexset(cmp);
    indexset.insert({0, 0});
    vector<vector<int>> ret;
    while (k-- and !indexset.empty()) {
      auto ind = *indexset.begin();
      auto [i, j] = ind;
      indexset.erase(indexset.begin());
      ret.push_back({nums1[i], nums2[j]});
      if (i + 1 < n1) indexset.insert({i + 1, j});
      if (j + 1 < n2) indexset.insert({i, j + 1});
    }
    return ret;
  }
};
```
## Tags

* [Priority queue](/Collections/priority-queue.md#priority-queue) > [K smallest/largest elements](/Collections/priority-queue.md#k-smallest-largest-elements)
