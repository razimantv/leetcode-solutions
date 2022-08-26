// https://leetcode.com/problems/check-if-word-equals-summation-of-two-words

class Solution {
 public:
  int val(const string& s) {
    int ret = 0;
    for (char c : s) ret = ret * 10 + c - 'a';
    return ret;
  }
  bool isSumEqual(string firstWord, string secondWord, string targetWord) {
    return val(firstWord) + val(secondWord) == val(targetWord);
  }
};
