// https://leetcode.com/problems/complement-of-base-10-integer

class Solution {
 public:
  int bitwiseComplement(int N) {
    int M = 1;
    do M <<= 1;
    while (M <= N);
    --M;
    return M ^ N;
  }
};
