// https://leetcode.com/problems/count-days-spent-together/

class Solution {
 public:
  int convert(string s) {
    vector<int> start{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    for (int i = 1; i <= 12; ++i) start[i] += start[i - 1];

    int month = (s[0] - '0') * 10 + s[1] - '0';
    int day = (s[3] - '0') * 10 + s[4] - '0';
    return start[month - 1] + day;
  }
  int countDaysTogether(string arriveAlice, string leaveAlice, string arriveBob,
                        string leaveBob) {
    int start = max(convert(arriveAlice), convert(arriveBob));
    int end = min(convert(leaveAlice), convert(leaveBob));
    return max(end - start + 1, 0);
  }
};
