// https://leetcode.com/problems/bitwise-xor-of-all-pairings/

class Solution {
 public:
  int xorAllNums(vector<int>& nums1, vector<int>& nums2) {
    int ret = 0;
    if (nums1.size() & 1)
      ret ^= accumulate(nums2.begin(), nums2.end(), 0, bit_xor<int>());
    if (nums2.size() & 1)
      ret ^= accumulate(nums1.begin(), nums1.end(), 0, bit_xor<int>());
    return ret;
  }
};
