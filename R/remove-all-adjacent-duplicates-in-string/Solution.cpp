// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string

class Solution {
 public:
  string removeDuplicates(string s) {
    int j = 1;
    for (int i = 1; s[i]; ++i) {
      if (j and (s[i] == s[j - 1]))
        --j;
      else
        s[j++] = s[i];
    }
    return s.substr(0, j);
  }
};
