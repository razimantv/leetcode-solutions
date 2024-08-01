# Determine if string halves are alike

[Problem link](https://leetcode.com/problems/determine-if-string-halves-are-alike)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/determine-if-string-halves-are-alike

class Solution {
 public:
  bool halvesAreAlike(string s) {
    int vowel = 0;
    for (char c : "AEIOU") vowel |= (1 << (c & 31));
    int tot = 0;
    for (int i = 0, j = s.size() - 1; i < j; ++i, --j)
      tot += (!(vowel & (1 << (s[i] & 31)))) - (!(vowel & (1 << (s[j] & 31))));
    return !tot;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
