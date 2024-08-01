# Count sorted vowel strings

[Problem link](https://leetcode.com/problems/count-sorted-vowel-strings)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-sorted-vowel-strings

class Solution {
 public:
  int countVowelStrings(int n) {
    return (n + 4) * (n + 3) * (n + 2) * (n + 1) / 24;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
