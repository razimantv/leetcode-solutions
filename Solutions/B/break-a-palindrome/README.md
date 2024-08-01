# Break a palindrome

[Problem link](https://leetcode.com/problems/break-a-palindrome)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/break-a-palindrome

class Solution {
 public:
  string breakPalindrome(string p) {
    int L = p.size();
    if (L == 1) return "";
    for (int i = 0; i < L / 2; ++i)
      if (p[i] > 'a') {
        p[i] = 'a';
        return p;
      }
    p[L - 1] = 'b';
    return p;
  }
};
```
## Tags

* [Palindrome](/Collections/palindrome.md#palindrome)
