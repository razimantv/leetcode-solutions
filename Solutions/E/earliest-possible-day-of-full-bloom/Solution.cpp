// https://leetcode.com/problems/earliest-possible-day-of-full-bloom/

class Solution {
 public:
  int earliestFullBloom(vector<int>& plantTime, vector<int>& growTime) {
    int n = plantTime.size();
    vector<pair<int, int>> work;
    for (int i = 0; i < n; ++i) work.push_back(plantTime[i], growTime[i]);
    sort(work.begin(), work.end(), [](auto a, auto b) {
      return a.first + max(a.second, b.first + b.second) <
             b.first + max(b.second, a.first + a.second);
    });

    int best = 0;
    for (int i = 0, cur = 0; i < n; ++i) {
      cur += work[i].first;
      best = max(best, cur + eork[i].second);
    }
    return best;
  }
};
