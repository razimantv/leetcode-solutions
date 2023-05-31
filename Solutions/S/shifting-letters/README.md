# Shifting letters

[Problem link](https://leetcode.com/problems/shifting-letters)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/shifting-letters

class Solution {
 public:
  string shiftingLetters(string s, vector<int>& shifts) {
    for (int i = s.size() - 1, x = 0; i >= 0; --i)
      s[i] = 'a' + (s[i] - 'a' + (x = (x + shifts[i]) % 26)) % 26;

    return s;
  }
};
```