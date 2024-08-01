# Number of adjacent elements with the same color

[Problem link](https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

class Solution {
 public:
  vector<int> colorTheArray(int n, vector<vector<int>>& queries) {
    int cnt{};
    vector<int> ret, clrs(n);
    for (auto q : queries) {
      int i = q[0], c = q[1];
      if (clrs[i]) {
        if (i and clrs[i] == clrs[i - 1]) --cnt;
        if (i < n - 1 and clrs[i] == clrs[i + 1]) --cnt;
      }

      clrs[i] = c;
      if (i and clrs[i] == clrs[i - 1]) ++cnt;
      if (i < n - 1 and clrs[i] == clrs[i + 1]) ++cnt;

      ret.push_back(cnt);
    }
    return ret;
  }
};
```
## Tags

* [Precomputation to answer queries efficiently with delta](/Collections/precomputation-to-answer-queries-efficiently-with-delta.md#precomputation-to-answer-queries-efficiently-with-delta)
