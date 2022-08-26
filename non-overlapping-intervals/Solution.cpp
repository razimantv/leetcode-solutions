// https://leetcode.com/problems/non-overlapping-intervals

class Solution {
 public:
  int eraseOverlapIntervals(vector<vector<int>>& intervals) {
    if (intervals.empty()) return 0;
    sort(intervals.begin(), intervals.end(),
         [](const vector<int>& a, const vector<int>& b) -> bool {
           return a[1] < b[1];
         });
    int cnt = 0, start = intervals[0][0];
    for (auto& i : intervals)
      if (i[0] >= start) {
        start = i[1];
        ++cnt;
      }
    return intervals.size() - cnt;
  }
};
