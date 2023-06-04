// https://leetcode.com/problems/minimize-string-length/

class Solution {
 public:
  int minimizedStringLength(string s) {
    unordered_set<char> ch(s.begin(), s.end());
    return ch.size();
  }
};
