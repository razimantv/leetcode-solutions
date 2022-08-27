// https://leetcode.com/problems/letter-case-permutation

class Solution {
 public:
  vector<string> letterCasePermutation(string S) {
    vector<string> ret{""};
    for (char c : S) {
      if (isdigit(c))
        for (auto& s : ret) s += c;
      else {
        int N = ret.size();
        for (int i = 0; i < N; ++i) {
          ret.push_back(ret[i]);
          ret.back() += toupper(c);
          ret[i] += tolower(c);
        }
      }
    }
    return ret;
  }
};
