// https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

class Solution {
 public:
  pair<vector<int>, vector<int>> oddeven(const vector<int>& v) {
    vector<int> odd, even;
    for (int x : v) ((x & 1) ? odd : even).push_back(x);
    sort(odd.begin(), odd.end());
    sort(even.begin(), even.end());
    return {odd, even};
  }

  long long work(const vector<int>& v1, const vector<int>& v2) {
    int n = v1.size();
    long long ret{};
    for (int i = 0; i < n; ++i) {
      if (v1[i] < v2[i]) ret += v2[i] - v1[i];
    }
    return ret / 2;
  }

  long long makeSimilar(vector<int>& nums, vector<int>& target) {
    auto [odd1, even1] = oddeven(nums);
    auto [odd2, even2] = oddeven(target);
    return work(odd1, odd2) + work(even1, even2);
  }
};
