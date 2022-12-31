from typing import List

class Solution():
	def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
		gr = [[] for x in range(n)]
		for x, y in edges:
			gr[x].append(y)
			gr[y].append(x)

		ans = n * [0]
		cnt = n * [1]
		root = 0

		def dfs(x, par, dep):
			ret = 1
			for y in gr[x]:
				if y != par:
					ret += dfs(y, x, dep+1)
					nonlocal root
					root += dep+1
			cnt[x] = ret
			return ret

		dfs(0, -1, 0)

		def dfs_2(x, par, prev_ans):
			ans[x] = prev_ans
			for y in gr[x]:
				if y != par:
					dfs_2(y, x, prev_ans + n - 2*cnt[y])

		dfs_2(0, -1, root)

		return ans
		