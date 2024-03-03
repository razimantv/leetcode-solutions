# https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        elems = sorted(list(set(nums)))
        pos = {x: i for i, x in enumerate(elems)}

        n, base = len(pos), 1
        while base < n:
            base <<= 1
        seg1, seg2 = [0] * (2 * base), [0] * (2 * base)

        def insert(seg, pos):
            pos += base
            while pos:
                seg[pos] += 1
                pos >>= 1

        def query(seg, pos):
            pos += base
            ret = 0
            while pos:
                if not (pos & 1):
                    ret += seg[pos ^ 1]
                pos >>= 1
            return ret

        nums1, nums2 = [nums[0]], [nums[1]]
        insert(seg1, pos[nums[0]])
        insert(seg2, pos[nums[1]])

        for x in nums[2:]:
            idx = pos[x]
            if (
                query(seg1, idx), -len(nums1)
            ) >= (
                query(seg2, idx), -len(nums2)
            ):
                insert(seg1, idx)
                nums1.append(x)
            else:
                insert(seg2, idx)
                nums2.append(x)

        return nums1 + nums2
