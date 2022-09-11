// https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution {
 public:
  int minGroups(vector<vector<int>>& intervals) {
    vector<pair<int, int>> endpoint;
    for (auto& x : intervals) {
      endpoint.push_back({x[0], -1});
      endpoint.push_back({x[1], 1});
    }

    sort(endpoint.begin(), endpoint.end());
    int ret = 0, cur = 0;
    for (auto [val, type] : endpoint) {
      ret = max(ret, cur -= type);
    }
    return ret;
  }
};
