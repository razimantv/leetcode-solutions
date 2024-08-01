# Frog jump ii

[Problem link](https://leetcode.com/problems/frog-jump-ii/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/frog-jump-ii/

class Solution {
 public:
  int maxJump(vector<int>& stones) {
    int n = stones.size();
    int best = max(stones[1] - stones[0], stones[n - 1] - stones[n - 2]);
    for (int i = 2; i < n; ++i) best = max(best, stones[i] - stones[i - 2]);
    return best;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
