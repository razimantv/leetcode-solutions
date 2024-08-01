# Furthest building you can reach

[Problem link](https://leetcode.com/problems/furthest-building-you-can-reach)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/furthest-building-you-can-reach

class Solution {
 public:
  int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
    multiset<int> big;
    int best = 0;
    for (int i = 1, n = heights.size(), used = 0; i < n; ++i) {
      big.insert(max(heights[i] - heights[i - 1], 0));
      if (big.size() > ladders) {
        if ((used += *big.begin()) > bricks) break;
        big.erase(big.begin());
      }
      ++best;
    }
    return best;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Priority queue](/Collections/priority-queue.md#priority-queue)
