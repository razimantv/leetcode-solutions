# Check if two string arrays are equivalent

[Problem link](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent

class Solution {
 public:
  bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
    string s1, s2;
    for (auto& w : word1) s1 += w;
    for (auto& w : word2) s2 += w;
    return s1 == s2;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
* [Suboptimal solution](/Collections/suboptimal-solution.md#suboptimal-solution)
