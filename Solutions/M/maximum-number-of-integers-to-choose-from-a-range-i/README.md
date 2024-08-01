# Maximum number of integers to choose from a range i

[Problem link](https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-number-of-integers-to-choose-from-a-range-i/

class Solution {
 public:
  int maxCount(vector<int>& banned, int n, int maxSum) {
    unordered_set<int> bad;
    for (int x : banned) bad.insert(x);

    int ret{};
    for (int i = 1, tot = 0; i <= n; ++i) {
      if (bad.count(i))
        continue;
      else if ((tot += i) > maxSum)
        break;
      else
        ++ret;
    }
    return ret;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Hashmap](/Collections/hashmap.md#hashmap)
