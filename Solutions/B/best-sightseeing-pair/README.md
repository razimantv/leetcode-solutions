# Best sightseeing pair

[Problem link](https://leetcode.com/problems/best-sightseeing-pair)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/best-sightseeing-pair

class Solution {
 public:
  int maxScoreSightseeingPair(vector<int>& values) {
    int prev = values[0], best = 0;
    for (int i = 1, n = values.size(); i < n; ++i) {
      best = max(best, prev + values[i] - i);
      prev = max(prev, values[i] + i);
    }
    return best;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Modify element with index](/Collections/array-scanning.md#modify-element-with-index)
* [Prefix](/Collections/prefix.md#prefix) > [Extremum](/Collections/prefix.md#extremum)
