// https://leetcode.com/problems/course-schedule-iii

class Solution {
 public:
  int scheduleCourse(vector<vector<int>>& courses) {
    sort(courses.begin(), courses.end(),
         [](const vector<int>& v1, const vector<int>& v2) {
           return v1[1] < v2[1];
         });

    int ret = 0;
    multiset<int, greater<int>> s;
    for (int i = 0, t = 0, n = courses.size(); i < n; ++i) {
      ++ret;
      t += courses[i][0];
      s.insert(courses[i][0]);

      if (t > courses[i][1]) {
        --ret;
        t -= *s.begin();
        s.erase(s.begin());
      }
    }
    return ret;
  }
};
