// https://leetcode.com/problems/remove-palindromic-subsequences

class Solution {
 public:
  int removePalindromeSub(string s) {
    if (s == "") return 0;
    for (int i = 0, n = s.size(), j = n - 1; i < j; ++i, --j)
      if (s[i] != s[j]) return 2;
    return 1;
  }
};
