# Check if a string is an acronym of words

[Problem link](https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

class Solution {
 public:
  bool isAcronym(vector<string>& words, string s) {
    string acr;
    for (auto w : words) acr += w[0];
    return acr == s;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
