// https://leetcode.com/problems/neighboring-bitwise-xor/

class Solution {
 public:
  bool doesValidArrayExist(vector<int>& derived) {
    return !accumulate(derived.begin(), derived.end(), 0, bit_xor<void>());
  }
};
