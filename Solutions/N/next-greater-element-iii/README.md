# Next greater element iii

[Problem link](https://leetcode.com/problems/next-greater-element-iii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/next-greater-element-iii

class Solution {
 public:
  int nextGreaterElement(int n) {
    string s = to_string(n), s2 = to_string(INT_MAX);
    if (!next_permutation(s.begin(), s.end())) return -1;

    if (s.size() == s2.size() and s2 < s) return -1;
    return stoi(s);
  }
};
```
## Tags

* [Permutation](/README.md#Permutation) > [Next/Previous](/README.md#Permutation-Next_Previous)
