from typing import List
import bisect

class SegTree:
    def __init__(self, a):
        self.n = len(a)
        self.inf = int(1e9+7)
        self.t = 4*self.n * [self.inf]
        self.build(0, 0, self.n, a)

    def build(self, v, vl, vr, a):
        if vl == vr-1:
            self.t[v] = a[vl]
            return
        mid = (vl+vr) // 2
        self.build(2*v+1, vl, mid, a)
        self.build(2*v+2, mid, vr, a)
        self.t[v] = min(self.t[2*v+1], self.t[2*v+2])

    def getmin(self, v, vl, vr, l, r):
        if vr <= l or vl >= r:
            return self.inf
        if vl >= l and vr <= r:
            return self.t[v]
        mid = (vl+vr) // 2
        return min(self.getmin(2*v+1, vl, mid, l, r), self.getmin(2*v+2, mid, vr, l, r))
    
    def __repr__(self):
        ret = ''
        for i in range(self.n):
            ret += repr(self.getmin(0, 0, self.n, i, i+1))+' '
        return ret

class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        sg = SegTree(A)
        n = len(A)
        d = {}
        for i, x in enumerate(A):
            if x not in d:
                d[x] = []
            d[x].append(i)

        ans = 0
        MD = int(1e9+7)

        for i in range(n):
            idx = bisect.bisect_left(d[A[i]], i)
            left, right = i, n if idx == len(d[A[i]])-1 else d[A[i]][idx+1]
            while right-left > 1:
                mid = (left+right) // 2
                if sg.getmin(0, 0, n, i, mid+1) == A[i]:
                    left = mid
                else:
                    right = mid
            rbound = left
            left, right = -1 if idx == 0 else d[A[i]][idx-1], i
            while right-left > 1:
                mid = (left+right) // 2
                if sg.getmin(0, 0, n, mid, i+1) == A[i]:
                    right = mid
                else:
                    left = mid
            lbound = right
            print(A[i], lbound, rbound)
            ans += A[i] * (i-lbound+1) * (rbound-i+1)
            ans %= MD
        return ans

# print(Solution().sumSubarrayMins(A=[71,55,82,55]))
print(Solution().sumSubarrayMins(A=[2, 1, 3, 1]))
# print(Solution().sumSubarrayMins(A=[3,1,2,4]))
# print(Solution().sumSubarrayMins(A=[11,81,94,43,3]))