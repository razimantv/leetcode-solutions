# Maximum bags with full capacity of rocks

[Problem link](https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

class Solution {
 public:
  int maximumBags(vector<int>& capacity, vector<int>& rocks, int add) {
    int n = capacity.size();
    for (int i = 0; i < n; ++i) capacity[i] -= rocks[i];
    sort(capacity.begin(), capacity.end());
    for (int i = 0; i < n; ++i)
      if (capacity[i] > add)
        return i;
      else
        add -= capacity[i];
    return n;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
