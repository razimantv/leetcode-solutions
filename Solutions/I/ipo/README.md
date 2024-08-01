# Ipo

[Problem link](https://leetcode.com/problems/ipo/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/ipo/

class Solution {
public:
  int findMaximizedCapital(int k, int w, vector<int> &profits,
                           vector<int> &capital) {
    int n = profits.size();
    vector<int> id(n);
    iota(id.begin(), id.end(), 0);
    sort(id.begin(), id.end(),
         [&](int i, int j) { return capital[i] < capital[j]; });

    multiset<int, greater<int>> pq;
    for (int i = 0, j = 0; i < k; ++i) {
      while (j < n and capital[id[j]] <= w)
        pq.insert(profits[id[j++]]);
      if (pq.empty())
        break;
      w += *pq.begin();
      pq.erase(pq.begin());
    }
    return w;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Index array](/Collections/sorting.md#index-array)
* [Priority queue](/Collections/priority-queue.md#priority-queue)
