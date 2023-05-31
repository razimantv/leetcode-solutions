# Shortest impossible sequence of rolls

[Problem link](https://leetcode.com/problems/shortest-impossible-sequence-of-rolls)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/shortest-impossible-sequence-of-rolls

class Solution {
 public:
  int shortestSequence(vector<int>& rolls, int k) {
    int n = rolls.size(), done = 0;
    unordered_set<int> s;
    for (int x : rolls) {
      s.insert(x);
      if (s.size() == k) ++done, s.clear();
    }
    return done + 1;
  }
};
```