# Maximum value of a string in an array

[Problem link](https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

class Solution {
 public:
  int maximumValue(vector<string>& strs) {
    int best = 0;
    for (string s : strs)
      if (*min_element(s.begin(), s.end()) >= '0' and
          *max_element(s.begin(), s.end()) <= '9')
        best = max(best, stoi(s));
      else
        best = max(best, (int)s.size());
    return best;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
