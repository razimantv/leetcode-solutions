// https://leetcode.com/problems/reduce-array-size-to-the-half

class Solution {
 public:
  int minSetSize(vector<int>& arr) {
    sort(arr.begin(), arr.end());

    vector<int> cnt;
    int N = arr.size();
    for (int i = 1, cur = 1;; ++i) {
      if (i == N) {
        cnt.push_back(cur);
        break;
      } else if (arr[i] == arr[i - 1])
        ++cur;
      else {
        cnt.push_back(cur);
        cur = 1;
      }
    }

    sort(cnt.begin(), cnt.end(), greater<int>());
    int ret = 0, tot = 0;
    for (int x : cnt) {
      ++ret;
      if (2 * (tot += x) >= N) break;
    }
    return ret;
  }
};
