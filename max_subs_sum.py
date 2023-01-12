class Node:
    def __init__(self, pref=0, suf=0, sub=0, sum=0):
        self.pref = pref
        self.suf = suf
        self.sub = sub
        self.sum = sum
        self.inf = int(1e9+228)
    
    def __repr__(self):
        return str(self.pref) + ' ' + str(self.suf) + ' ' + str(self.sub) + ' ' + str(self.sum)

class SegTree:
    def __init__(self, a):
        self.n = len(a)
        self.t = 4*self.n * [Node(0, 0, 0, 0)]
        self.inf = int(1e9+228)
        self.build(0, 0, self.n, a)
    
    def build(self, v, vl, vr, a) -> None:
        if vl == vr-1:
            self.t[v] = Node(a[vl], a[vl], a[vl], a[vl])
            return
        
        mid = (vl+vr) // 2
        node_l, node_r = 2*v+1, 2*v+2
        self.build(node_l, vl, mid, a)
        self.build(node_r, mid, vr, a)

        self.t[v].pref = max(self.t[node_l].pref, self.t[node_l].sum + self.t[node_r].pref)
        self.t[v].suf = max(self.t[node_r].suf, self.t[node_r].sum + self.t[node_l].suf)
        self.t[v].sub = max(self.t[node_l].sum, self.t[node_r].sum, self.t[node_l].suf + self.t[node_r].pref)
        self.t[v].sum = self.t[node_l].sum + self.t[node_r].sum
    
    def modify(self, v, vl, vr, idx, val) -> None:
        if vl == vr-1:
            self.t[v] = Node(val, val, val, val)
            return
        
        mid = (vl+vr) // 2
        left, right = 2*v+1, 2*v+2
        if idx < mid:
            self.modify(left, vl, mid, idx, val)
        else:
            self.modify(right, mid, vr, idx, val)
        
        self.t[v].pref = max(self.t[left].pref, self.t[left].sum + self.t[right].pref)
        self.t[v].suf = max(self.t[right].suf, self.t[right].sum + self.t[left].suf)
        self.t[v].sub = max(self.t[left].sum, self.t[right].sum, self.t[left].suf + self.t[right].pref)
        self.t[v].sum = self.t[left].sum + self.t[right].sum
    
    def go(self, v, vl, vr, l, r) -> Node:
        if vl >= l and vr <= r:
            return self.t[v]
        
        if l >= vr or r <= vl:
            return Node(-self.inf, -self.inf, -self.inf, -self.inf)
        
        mid = (vl+vr) // 2
        res = Node()
        left = self.go(2*v+1, vl, mid, l, r)
        right = self.go(2*v+2, mid, vr, l, r)

        res.pref = max(left.pref, left.sum + right.pref)
        res.suf = max(right.suf, right.sum + left.suf)
        res.sub = max(left.sum, right.sum, left.suf + right.pref)
        res.sum = left.sum + right.sum
        return res
    
    def __repr__(self) -> str:
        ret = ''
        for i in range(self.n):
            ret += repr(self.go(0, 0, n, i, i+1).sub) + ' '
        return ret

nums = [1,2,5,6,1]
removeQueries = [0,3,2,4,1]
n = len(nums)
inf = int(1e9+228)
ans = []

st = SegTree(nums)

print(st.go(0, 0, n, 0, 2).pref, st.go(0, 0, n, 0, 2).suf, st.go(0, 0, n, 0, 2).sub, st.go(0, 0, n, 0, 2).sum)

def go(v, vl, vr):
    nd = st.go(0, vl, vr, vl, vr)
    print(f'[{vl}, {vr}] {nd.pref, nd.suf, nd.sub, nd.sum}')

    if vl == vr-1:
        return
    
    mid = (vl+vr) // 2
    go(2*v+1, vl, mid)
    go(2*v+2, mid, vr)

# go(0, 0, n)

for pz in removeQueries:
    # print(st)
    st.modify(0, 0, n, pz, -inf)
    ans.append(st.go(0, 0, n, 0, n).sub)

# print(ans)