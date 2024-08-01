# Eliminate maximum number of monsters

[Problem link](https://leetcode.com/problems/eliminate-maximum-number-of-monsters)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/eliminate-maximum-number-of-monsters

class Solution {
 public:
  int eliminateMaximum(vector<int>& dist, vector<int>& speed) {
    int N = dist.size();
    for (int i = 0; i < N; ++i) dist[i] = (dist[i] + speed[i] - 1) / speed[i];
    sort(dist.begin(), dist.end());

    int ret = 0;
    for (int i = 0; i < N; ++i)
      if (dist[i] <= i)
        break;
      else
        ++ret;
    return ret;
  }
};
```
## Tags

* [Sorting](/Collections/sorting.md#sorting) > [Custom](/Collections/sorting.md#custom)
* [Greedy](/Collections/greedy.md#greedy)
