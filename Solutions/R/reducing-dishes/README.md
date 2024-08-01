# Reducing dishes

[Problem link](https://leetcode.com/problems/reducing-dishes)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/reducing-dishes

class Solution {
 public:
  int maxSatisfaction(vector<int>& ar) {
    sort(ar.begin(), ar.end(), greater<int>());

    int best = 0, cur = 0, pref = 0;
    for (int n : ar)
      if ((cur += (pref += n)) > best) best = cur;
    return best;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
