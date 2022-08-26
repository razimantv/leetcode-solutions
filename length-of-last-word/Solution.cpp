// https://leetcode.com/problems/length-of-last-word

class Solution {
 public:
  int lengthOfLastWord(string s) {
    istringstream iss(s);
    string a;
    while (iss >> a)
      ;
    return a.size();
  }
};
