# Longest subsequence repeated k times

[Problem link](https://leetcode.com/problems/longest-subsequence-repeated-k-times/)

## Observations

- The problem asks for the longest subsequence that can be repeated `k` times.
- A key observation is that the length of the resulting subsequence will be at most `n // k`, where `n` is the length of the input string `s`. This is because if a subsequence of length `L` is repeated `k` times, it will require `L * k` characters from the original string. Given than `n < 8k` from the constraints, there can be at most 7 characters in the subsequence.
- The characters that can form the subsequence must have a frequency of at least `k` in the original string. We can filter out characters that do not meet this criterion.

## Algorithm

The solution uses a "generate and test" approach:

1.  **Character Filtering**:
    -   First, count the frequency of each character in the input string `s`.
    -   Create a list of characters that can potentially form the subsequence. A character `c` can appear in the subsequence `m` times only if its frequency in `s` is at least `m * k`. The code creates a list `chars` containing each character `c` repeated `count(c) // k` times.

2.  **Generate Candidates**:
    -   From the filtered list of characters, generate all possible permutations of all possible lengths.
    -   These permutations are the candidate subsequences.
    -   The candidates are stored in a set `S` to avoid duplicates and then sorted in descending order of length, and lexicographically for ties. This ensures that we find the longest and lexicographically largest subsequence first.

3.  **Test Candidates**:
    -   Iterate through the sorted candidate subsequences.
    -   For each candidate, check if it can be formed by repeating it `k` times as a subsequence of `s`.
    -   The `work` function performs this check. It iterates `k` times, and in each iteration, it tries to find the candidate subsequence within the remaining part of `s`.
    -   If a candidate is found to be a valid repeated subsequence, it is returned as the answer.
    -   If no such subsequence is found (e.g., no character appears `k` times), an empty string is returned.

## Complexity

-   **Time Complexity**: The number of permutations of the `chars` list can be large. If the length of `chars` is `m`, the number of permutations is `O(m!)`. For each permutation, the `work` function takes `O(n)`. However, this approach is feasible because the subsequence can have at most 7 characters.

## Solutions


### Solution.py
```py
# https://leetcode.com/problems/longest-subsequence-repeated-k-times/

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n, ctr = len(s), Counter(s)
        chars = sum(([c] * (x // k) for c, x in ctr.items()), start=[])
        if not chars:
            return ''
        L = len(chars)
        S = set(
            p[:i] for p in map(tuple, permutations(chars))
            for i in range(1, L + 1)
        )
        S = sorted(S, key=lambda x: (len(x), x), reverse=True)

        def work(t):
            i = 0
            for j in range(k):
                for c in t:
                    while i < n and s[i] != c:
                        i += 1
                    else:
                        if i == n:
                            return False
                        i += 1
            return True

        for poss in S:
            if work(poss):
                return ''.join(poss)
        return ''
```
## Tags

* [String](/Collections/string.md#string) > [Subsequence](/Collections/string.md#subsequence)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Counter](/Collections/hashmap.md#counter)
* [Sorting](/Collections/sorting.md#sorting) > [Custom](/Collections/sorting.md#custom)
