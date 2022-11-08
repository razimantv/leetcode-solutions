// https://leetcode.com/problems/make-the-string-great

class Solution {
 public:
  bool bad(char a, char b) { return ((a ^ b) == 32); }
  string makeGood(string s) {
    string ret;
    for (char c : s) {
      if (!ret.empty() and bad(c, ret.back()))
        ret.pop_back();
      else
        ret += c;
    }
    return ret;
  }
};
