# Make string a subsequence using cyclic increments

[Problem link](https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

class Solution {
 public:
  bool canMakeSubsequence(string str1, string str2) {
    int pos{};
    for (int i = 0; str1[i] and str2[pos]; ++i)
      if (str2[pos] == str1[i] or (str2[pos] % 26) == ((str1[i] + 1) % 26))
        ++pos;
    return !str2[pos];
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [String](/Collections/string.md#string) > [Subsequence](/Collections/string.md#subsequence)
