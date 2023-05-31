# Valid palindrome ii

[Problem link](https://leetcode.com/problems/valid-palindrome-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/valid-palindrome-ii

class Solution {
 public:
  bool validPalindrome(string s) {
    int n = s.size(), l = 0, r = n - 1;
    while (l < r and s[l] == s[r]) ++l, --r;
    if (l >= r) return true;
    int a = (n - 2) >> 1, b = a + (n & 1);
    while (a >= l and s[a] == s[b]) --a, ++b;
    if (a < l) return true;
    a = n >> 1, b = a + (n & 1);
    while (b <= r and s[a] == s[b]) --a, ++b;
    return b > r;
  }
};
```