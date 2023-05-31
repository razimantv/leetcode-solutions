# Shortest palindrome

[Problem link](https://leetcode.com/problems/shortest-palindrome)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/shortest-palindrome

class Solution {
 public:
  string shortestPalindrome(string s) {
    long long p = 354745078340568241, fwhash = 0, bwhash = 0, pow26 = 1;
    int L = s.size();
    int best = 0;
    for (int i = 0; i < L; ++i) {
      fwhash = (fwhash * 26 + (s[i] - 'a')) % p;
      bwhash = (bwhash + (pow26 * (s[i] - 'a')) % p) % p;
      if (fwhash == bwhash) best = i + 1;
      pow26 = (pow26 * 26) % p;
    }

    string ret = s.substr(best);
    reverse(ret.begin(), ret.end());
    return ret + s;
  }
};
```