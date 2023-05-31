# Find the divisibility array of a string

[Problem link](https://leetcode.com/problems/find-the-divisibility-array-of-a-string/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-divisibility-array-of-a-string/

class Solution {
 public:
  vector<int> divisibilityArray(string word, int m) {
    int n = word.size();
    vector<int> ret(n);
    for (long long i = 0, pref = 0; i < n; ++i) {
      pref = (pref * 10 + word[i] - '0') % m;
      if (!pref) ret[i] = 1;
    }
    return ret;
  }
};
```
## Tags

* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Basic](/README.md#Mathematics-Number_theory-Basic)
