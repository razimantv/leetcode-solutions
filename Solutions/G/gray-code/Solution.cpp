// https://leetcode.com/problems/gray-code

class Solution {
 public:
  vector<int> grayCode(int n) {
    int M = 1 << n;
    vector<int> ret(M);
    for (int i = 0; i < M; ++i) ret[i] = i ^ (i >> 1);
    return ret;
  }
};
