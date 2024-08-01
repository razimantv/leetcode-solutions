# Determine if two events have conflict

[Problem link](https://leetcode.com/problems/determine-if-two-events-have-conflict/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/determine-if-two-events-have-conflict/

class Solution {
 public:
  int conv(string s) {
    int h = (s[0] - '0') * 10 + s[1] - '0';
    int m = (s[3] - '0') * 10 + s[4] - '0';
    return h * 60 + m;
  }
  bool haveConflict(vector<string>& event1, vector<string>& event2) {
    int start1 = conv(event1[0]), end1 = conv(event1[1]);
    int start2 = conv(event2[0]), end2 = conv(event2[1]);
    return min(end1, end2) >= max(start1, start2);
  }
};
```
## Tags

* [Intervals](/Collections/intervals.md#intervals) > [Overlap](/Collections/intervals.md#overlap)
