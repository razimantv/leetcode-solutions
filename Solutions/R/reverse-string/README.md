# Reverse string

[Problem link](https://leetcode.com/problems/reverse-string)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/reverse-string

class Solution {
 public:
  void reverseString(vector<char>& s) {
    int N = s.size();
    for (int i = 0, j = N - 1; i < j; ++i, --j) swap(s[i], s[j]);
  }
};
```