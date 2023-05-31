# Smallest string with a given numeric value

[Problem link](https://leetcode.com/problems/smallest-string-with-a-given-numeric-value)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/smallest-string-with-a-given-numeric-value

class Solution {
 public:
  string getSmallestString(int n, int k) {
    k -= n;
    string ret(n, ' ');
    for (int i = n - 1; i >= 0; --i)
      ret[i] = (char)('a' + min(k, 25)), k -= min(k, 25);
    return ret;
  }
};
```