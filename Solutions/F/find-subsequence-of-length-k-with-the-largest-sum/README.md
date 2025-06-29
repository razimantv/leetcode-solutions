# Find subsequence of length k with the largest sum

[Problem link](https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/)

## Observations

- The problem asks for a subsequence of length `k` with the largest possible sum.
- The order of elements in the output subsequence must be the same as their relative order in the original input array `nums`.
- To get the largest sum, we should pick the `k` largest numbers from `nums`.
- If there are multiple numbers with the same value, we might need to include some of them but not all.

## Algorithm

The solution identifies the `k` largest elements that must form the subsequence and then constructs the subsequence while preserving the original order.

1.  **Identify the Threshold Value**:
    -   Instead of sorting the entire `nums` array, the algorithm first finds the frequency of each number in `nums`.
    -   It then sorts these number-frequency pairs in descending order based on the number.
    -   It iterates through this sorted list to find the "threshold" or "middle" value (`mid`). This `mid` is the smallest number that must be included in our subsequence of `k` largest elements.
    -   The logic determines exactly how many instances of `mid` (`midc`) are needed to reach a total of `k` elements, after having included all numbers greater than `mid`.

2.  **Construct the Subsequence**:
    -   The algorithm iterates through the original `nums` array from left to right.
    -   It includes any number `x` in the result if `x` is greater than the `mid` value.
    -   If `x` is equal to `mid`, it includes it only if we still need more instances of `mid` (i.e., `midc > 0`). `midc` is decremented each time an instance of `mid` is added.
    -   This process ensures that the final `ret` list contains the `k` largest elements from `nums` while maintaining their original relative order.

## Complexity

-   **Time Complexity**: `O(N log N)`, where `N` is the number of unique elements in `nums`. The dominant step is sorting the items from the frequency counter. If `U` is the number of unique elements, this is `O(U log U)`. The final scan of `nums` takes `O(N)`. Since `U <= N`, the overall complexity is bounded by `O(N log N)` in the case where all elements are unique.
-   **Space Complexity**: `O(U)` to store the frequency counter, where `U` is the number of unique elements in `nums`.

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/

class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        ctr = sorted(list(Counter(nums).items()), reverse=True)
        used = 0
        for x, c in ctr:
            if used + c >= k:
                mid, midc = x, k - used
                break
            used += c

        ret = []
        for x in nums:
            if x > mid:
                ret.append(x)
            elif x == mid and midc:
                ret.append(x)
                midc -= 1
        return ret
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Greedy](/Collections/greedy.md#greedy)
