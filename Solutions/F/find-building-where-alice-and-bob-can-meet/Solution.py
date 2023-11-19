# https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        qd = defaultdict(list)
        for i, (u, v) in enumerate(queries):
            qd[max(u, v)].append((i, min(u, v)))

        n = len(heights)
        mono = []
        for i in range(n-1, -1, -1):
            while mono and heights[mono[-1]] <= heights[i]:
                mono.pop()
            mono.append(i)

            for q, j in qd[i]:
                if j == i or heights[j] < heights[i]:
                    queries[q] = i
                    continue

                h = max(heights[i], heights[j])
                start, end = -1, len(mono)
                while end - start > 1:
                    mid = (start + end) // 2
                    if heights[mono[mid]] > h:
                        start = mid
                    else:
                        end = mid
                queries[q] = mono[start] if start > -1 else -1

        return queries
