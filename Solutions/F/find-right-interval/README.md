# Find right interval

[Problem link](https://leetcode.com/problems/find-right-interval)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-right-interval

class Solution {
 public:
  vector<int> findRightInterval(vector<vector<int>>& intervals) {
    int N = intervals.size();
    vector<pair<vector<int>, int>> v(N);
    for (int i = 0; i < N; ++i) v[i] = {intervals[i], i};
    sort(v.begin(), v.end());
    vector<int> ret(N);
    for (auto in : v) {
      auto in2 = in;
      in2.first[0] = in2.first[1];
      int pos = lower_bound(v.begin(), v.end(), in2) - v.begin();
      ret[in.second] = (pos == N) ? -1 : v[pos].second;
    }
    return ret;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Remembering index](/Collections/sorting.md#remembering-index)
* [Binary search](/Collections/binary-search.md#binary-search)
