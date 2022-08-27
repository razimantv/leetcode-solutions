// https://leetcode.com/problems/perform-string-shifts

class Solution {
 public:
  string stringShift(string s, vector<vector<int>>& shift) {
    int N = s.size(), F = 0;
    for (auto f : shift) F += (f[0] == 0 ? f[1] : (N - f[1]));
    F %= N;
    return s.substr(F) + s.substr(0, F);
  }
};
