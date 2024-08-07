# Split array largest sum

[Problem link](https://leetcode.com/problems/split-array-largest-sum)

## Solution

### The problem

Given an array of non-negative integers (nums), find a way to partition the array into m pieces such that the largest sum among the m pieces is minimised.

### Finding the first piece of the partition

Let us say we are trying to generate the first piece of the partition. We take the first element, the second and so on, and we need to stop at some point. Where do we stop?

* If we stop too late, we will get a high sum for the first piece itself, making it suboptimal
* If we stop too early, the first piece will get a low sum. But it will force us to make high sums in later pieces, making it suboptimal.

So we need to stop at just the right point. But how?

### Identify the issue

The reason we didn't know where to stop was that we didn't know what sum we were trying to achieve. If we knew that we were trying to stay ≤ target sum x, we could keep adding elements to the first piece till we cross the sum x, and stop at the previous element. We clearly cannot stop later, and it is not useful to stop any earlier. Do the same for the second piece and so on. If we are able to exhaust the elements in this array in m pieces without letting any sum go > x, a valid partition with sum ≤ x exists, and not otherwise. This **greedy algorithm** is thus guaranteed to find a solution if it exists.

This gives us the first crucial piece needed to solve the problem:

### Invert the problem

Instead of trying to find the partition with the minimum largest sum x, check whether it is possible to make a partition where all pieces have sum ≤ x.

Why does this help us to solve the problem? Here is where monotonicity comes in

### Monotonicity

In the greedy algorithm mentioned above, suppose that we found that a good partition exists for sum ≤ x. What if we wanted to check whether a good partition exists for sum ≤ x+1? Every piece we make in the greedy algorithm for x+1 will end at the same point as the piece for x, or later. Thus the greedy algorithm will work for x+1 as well.

More generally, if x works, all y>x will work too. Inverting this statement, if x does not work, no y<x will work.

That gives us the final piece

### Binary search

Suppose we could find two values start and end such that start < end and the greedy algorithm fails for start and succeeds for end. Then by monotonicity above, the required answer x has the property start < x ≤ end. We can repeatedly bisect the range and find x in logarithmic time.

All that remains is to find a value of start and end.

* The largest element will be part of some partition, so the minimum largest sum cannot be less than this element. So it is enough to take start = max(array) - 1 because the greedy will fail on start
* Even if we put all elements into one partition, the sum cannot go more than the sum of the array. So put end = sum(array) because greedy will succeed

And that is it.

### Putting everything together

* `possible(x)`: Greedy algorithm to check whether a partition of the array exists such that all pieces have sum ≤x:
   * Start from the first element of the array. Keep a count of pieces formed and current sum  (both initialised to 0)
   * When processing an element, add its value to current sum. If the sum goes above x, increment piece count and set current sum to current element. If piece count is equal to m, it is not possible to partition the array. Return false
   * If piece count < m after processing the array, return true
* Main algorithm:
   * Initialise start = max(array) - 1, end = sum(array). Keep the invariant that possible (start) is always false and possible(end) is always true
   * While end - start > 1
      * mid = (start + end) / 2
      * If possible(mid), end = mid. Otherwise, start = mid
   * When you break out of the while loop, the value of end is the required answer.

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/split-array-largest-sum

class Solution {
 public:
  bool poss(const vector<int>& nums, int tot, int m) {
    for (int i = 0, n = nums.size(), cur = 0; i < n; ++i) {
      if ((cur += nums[i]) > tot) {
        if (!--m) return false;
        cur = nums[i];
      }
    }
    return true;
  }
  int splitArray(const vector<int>& nums, int m) {
    int start = 0, end = 0;
    for (int x : nums) start = max(start, x), end += x;
    --start;

    while (end - start > 1) {
      int mid = (end + start) >> 1;
      (poss(nums, mid, m) ? end : start) = mid;
    }
    return end;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
* [Greedy](/Collections/greedy.md#greedy)
