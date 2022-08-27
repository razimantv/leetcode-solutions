// https://leetcode.com/problems/largest-divisible-subset

class Solution {
 public:
  vector<int> largestDivisibleSubset(vector<int>& nums) {
    if (nums.empty()) return {};

    sort(nums.begin(), nums.end());
    map<int, pair<int, int>> prev;
    pair<int, int> best = {1, nums[0]};
    for (int n : nums) {
      pair<int, int> cur = {1, -1};
      for (int i = 1; i * i <= n; i++) {
        if (n % i) continue;
        if (prev.count(i)) {
          auto p = prev[i];
          if (p.first >= cur.first) cur = {p.first + 1, i};
        }
        if (i * i == n) break;
        if (prev.count(n / i)) {
          auto p = prev[n / i];
          if (p.first >= cur.first) cur = {p.first + 1, n / i};
        }
      }
      if (cur.first > best.first) best = {cur.first, n};
      prev[n] = cur;
    }

    vector<int> ans;
    for (int i = best.second; i != -1; i = prev[i].second) ans.push_back(i);
    return ans;
  }
};
