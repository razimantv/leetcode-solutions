// https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array

class Solution {
 public:
  int maxValue(int n, int index, int maxSum) {
    maxSum -= n;
    int start = 0, end = maxSum + 1;

    while (end - start > 1) {
      int mid = (start + end) / 2;
      long long cursum = mid;
      if (index > mid)
        cursum += (mid * (long long)(mid - 1)) / 2;
      else
        cursum += ((mid - 1 + mid - index) * (long long)(index)) / 2;
      if (n - 1 - index > mid)
        cursum += (mid * (long long)(mid - 1)) / 2;
      else
        cursum +=
            ((mid - 1 + mid - (n - 1 - index)) * (long long)(n - 1 - index)) /
            2;
      // std::cout << start << " " << end << " " << mid << " " << cursum <<
      // "\n";
      if (cursum > maxSum)
        end = mid;
      else
        start = mid;
    }
    return start + 1;
  }
};
