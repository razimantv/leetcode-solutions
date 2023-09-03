// https://leetcode.com/problems/count-of-interesting-subarrays/

class Solution {
 public:
  long long countInterestingSubarrays(vector<int>& nums, int modulo, int k) {
    unordered_map<int, int> cnt;
    cnt[0] = 1;
    int pref{};
    long long ret{};
    for (int x : nums) {
      pref = (pref + (x % modulo == k)) % modulo;
      ret += cnt[(pref + modulo - k) % modulo];
      ++cnt[pref];
    }
    return ret;
  }
};
