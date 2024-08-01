# Dota2 senate

[Problem link](https://leetcode.com/problems/dota2-senate)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/dota2-senate

class Solution {
 public:
  string predictPartyVictory(string senate) {
    int r{}, d{}, diff{};
    for (char c : senate) ++(c == 'R' ? r : d);
    while (r and d) {
      string next;
      for (char c : senate) {
        if (c == 'R') {
          if (diff++ < 0)
            --r;
          else
            next += c;
        } else {
          if (diff-- > 0)
            --d;
          else
            next += c;
        }
      }
      senate = next;
    }
    return r ? "Radiant" : "Dire";
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Array scanning](/Collections/array-scanning.md#array-scanning)
