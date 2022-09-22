// https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution {
 public:
  string reverseWords(string s) {
    istringstream iss(s);
    string ret, cur;
    while (iss >> cur) {
      if (ret.size()) ret += " ";
      reverse(cur.begin(), cur.end());
      ret += cur;
    }
    return ret;
  }
};
