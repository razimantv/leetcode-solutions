// https://leetcode.com/problems/to-lower-case

class Solution {
 public:
  string toLowerCase(string s) {
    for (char& c : s) c |= ' ';
    return s;
  }
};
