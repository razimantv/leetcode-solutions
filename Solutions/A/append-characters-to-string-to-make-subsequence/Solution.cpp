// https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution {
 public:
  int appendCharacters(string s, string t) {
    int i = 0, j = 0;
    while (s[i] and t[j])
      if (s[i++] == t[j]) ++j;
    return t.size() - j;
  }
};
