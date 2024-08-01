# Maximum area of a piece of cake after horizontal and vertical cuts

[Problem link](https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts

class Solution {
 public:
  long long get(vector<int>& vec, int L) {
    sort(vec.begin(), vec.end());
    int ret = max(vec[0], L - vec.back());
    for (int i = 1, n = vec.size(); i < n; ++i)
      ret = max(ret, vec[i] - vec[i - 1]);
    return ret;
  }
  int maxArea(int h, int w, vector<int>& hc, vector<int>& vc) {
    return (get(hc, h) * get(vc, w)) % 1'000'000'007;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting)
