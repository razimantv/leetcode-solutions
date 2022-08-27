// https://leetcode.com/problems/counting-bits

class Solution {
 public:
  vector<int> countBits(int num) {
    vector<int> ret(num + 1);
    for (int i = 1; i <= num; ++i) {
      ret[i] = ((i & 1) ? ret[i - 1] + 1 : ret[i >> 1]);
    }
    return ret;
  }
};
