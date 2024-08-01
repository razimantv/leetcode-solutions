# Remove stones to minimize the total

[Problem link](https://leetcode.com/problems/remove-stones-to-minimize-the-total/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution {
 public:
  int minStoneSum(vector<int>& piles, int k) {
    multiset<int, greater<int>> s;
    for (int x : piles) s.insert(x);

    while (k--) {
      int u = *s.begin();
      s.erase(s.begin());
      s.insert(u - u / 2);
    }

    return accumulate(s.begin(), s.end(), 0);
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Priority queue](/Collections/priority-queue.md#priority-queue)
