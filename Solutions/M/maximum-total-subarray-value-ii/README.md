# Maximum total subarray value ii

[Problem link](https://leetcode.com/problems/maximum-total-subarray-value-ii/)

We need to find the sum of the values of the $k$ subarrays that have the largest values (that is, difference between its maximum and minimum elements): $\text{val}(S) = \max(S) - \min(S)$.
Since the number of subarrays is $O(N^2)$, we cannot iterate through all of them. We need a more efficient approach combining **Binary Search on the Answer**, **Monotonic Stacks**, and **Two Pointers**.

## Key Observations

1.  **Monotonicity of Subarray Value**: For a fixed ending position $i$, as we move the starting position $j$ further to the left (from $i$ down to $0$), the subarray $[j, i]$ grows. As a subarray grows, its maximum can only increase (or stay the same) and its minimum can only decrease (or stay the same). Therefore, the value $V(j, i) = \max - \min$ is **non-decreasing** as $j$ decreases.
2.  **Binary Search on the Threshold**: To find the sum of the top $k$ values, we can binary search for a threshold $X$ such that there are at least $k$ subarrays with a value $\ge X$.
3.  **Separating Max/Min**: The sum of values $(\max - \min)$ over a set of subarrays can be computed as $(\sum \max) - (\sum \min)$. As the sums for max and min get separated, we can use monotonic stacks to solve the problem.

## Algorithm

We search for the largest value `diff` such that the number of subarrays with $\max - \min \ge \text{diff}$ is at least $k$.

- **Range**: `[0, max(nums) - min(nums)]`.
- **Predicate**: A helper function `work(diff)` that returns the count of subarrays with value $\ge \text{diff}$. We will also find the sum of their values efficiently in this function.

For each index $i$ (treating it as the end of a subarray), we want to find how many starting indices $j \in [0, i]$ satisfy $V(j, i) \ge \text{diff}$. We will use monotonic stacks to solve this.

### Monotonic Stacks and Prefix Sums
We maintain two monotonic stacks:

- `monoinc`: Indices of elements in increasing order (to track minimums).
- `monodec`: Indices of elements in decreasing order (to track maxima).

We also maintain `incsum` and `decsum` to store the sum of minimums and maxima of all subarrays ending at $i$. When a new element $x$ is processed:

- If $x$ is smaller than previous elements, it "takes over" their ranges as the new minimum. 
- The sum of minimums for all $j \in [0, i]$ ending at $i$ is updated: `new_sum = old_sum + (i - last_index) * x`.

`monodec` and `decsum` are updated similarly for maxima.

### Two Pointers for the Threshold
Because $V(j, i)$ is monotonic with respect to $j$, there exists a boundary `last` such that for all $j \le \text{last}$, $V(j, i) \ge \text{diff}$. 

- As $i$ increases, `last` also moves to the right.
- We use two pointers (`p1` and `p2`) to traverse the monotonic stacks to find the first index where the difference between the max (from `monodec`) and min (from `monoinc`) is at least `diff`.

The position of `last` determines the number of valid starting indices if the endpoint is $i$, and we can use the prefix sums to compute the total sum of $(\max - \min)$ for these subarrays. Adding up the contributions for all $i$ gives us the total count and sum of subarrays with value $\ge \text{diff}$.

Since multiple subarrays might have the same value as our threshold `start`, the binary search might find `cnt > k`. 
We need to be careful to remove the "excess" subarrays from the final sum.

## Complexity Analysis

-   **Time Complexity**: 
    -   The `work` function runs in $O(N)$ time. Each element is pushed and popped from the monotonic stacks at most once. The pointers `p1`, `p2`, and `last` only move forward.
    -   The binary search takes $O(\log(\max(nums)))$ steps.
    -   **Total**: $O(N \log (\text{MaxDiff}))$, where $N$ is the length of the array.
-   **Space Complexity**: $O(N)$ to store the monotonic stacks and prefix sum arrays.

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/maximum-total-subarray-value-ii/

class Solution:
    def maxTotalValue(self, nums: list[int], k: int) -> int:
        def work(diff):
            monoinc, monodec = [-1], [-1]
            incsum, decsum = [0], [0]
            last, p1, p2, cnt, tot = -1, 1, 1, 0, 0
            for i, x in enumerate(nums):
                while monoinc[-1] > -1 and x <= nums[monoinc[-1]]:
                    monoinc.pop()
                    incsum.pop()
                    p1 = min(p1, len(monoinc))
                while monodec[-1] > -1 and x >= nums[monodec[-1]]:
                    monodec.pop()
                    decsum.pop()
                    p2 = min(p2, len(monodec))
                incsum.append(incsum[-1] + (i - monoinc[-1]) * x)
                decsum.append(decsum[-1] + (i - monodec[-1]) * x)
                monoinc.append(i)
                monodec.append(i)

                while last + 1 <= i and nums[monodec[p2]] - nums[monoinc[p1]] >= diff:
                    last = min(monodec[p2], monoinc[p1])
                    if monoinc[p1] == last:
                        p1 += 1
                    if monodec[p2] == last:
                        p2 += 1
                cnt += last + 1
                tot += (decsum[-1] - incsum[-1]) if last == i else (
                    (decsum[p2] - (monodec[p2] - last) * nums[monodec[p2]]) - 
                    (incsum[p1] - (monoinc[p1] - last) * nums[monoinc[p1]])
                )
            return cnt, tot

        start, end = 0, max(nums) - min(nums) + 1
        while end - start > 1:
            mid = (start + end) // 2
            if work(mid)[0] >= k:
                start = mid
            else:
                end = mid
        
        cnt, tot = work(start)
        return tot - (cnt - k) * start
```
## Tags

* [Stack](/Collections/stack.md#stack) > [Monotonic stack](/Collections/stack.md#monotonic-stack)
* [Binary search](/Collections/binary-search.md#binary-search)
* [Two pointers](/Collections/two-pointers.md#two-pointers)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
