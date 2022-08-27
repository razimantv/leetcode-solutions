// https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and

class Solution {
 public:
  int getXORSum(vector<int>& arr1, vector<int>& arr2) {
    int n1 = 0, n2 = 0;
    for (int n : arr1) n1 ^= n;
    for (int n : arr2) n2 ^= n;
    return n1 & n2;
  }
};
