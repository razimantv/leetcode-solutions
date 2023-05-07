// https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

class Solution {
 public:
  vector<int> longestObstacleCourseAtEachPosition(vector<int>& obstacles) {
    vector<int> ret, lis;
    for (int x : obstacles) {
      int len = upper_bound(lis.begin(), lis.end(), x) - lis.begin();
      if (len == lis.size())
        lis.push_back(x);
      else
        lis[len] = x;
      ret.push_back(len + 1);
    }
    return ret;
  }
};
