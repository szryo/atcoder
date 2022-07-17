from collections import deque

class UnionFind:
    '0-indexed'
    from typing import List

    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n

    def unite(self, x, y) -> int:
        'xとyを併合'
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return 0
        if self.parent[x] > self.parent[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        return self.parent[x]

    def is_same(self, x, y) -> bool:
        'xとyが同じ連結成分か判定'
        return self.root(x) == self.root(y)

    def root(self, x) -> int:
        'xの根を取得'
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def size(self, x) -> int:
        'xが属する連結成分のサイズを取得'
        return -self.parent[self.root(x)]

    def all_sizes(self) -> List[int]:
        '全連結成分のサイズのリストを取得'
        '計算量: O(N)'
        sizes = []
        for i in range(self.n):
            size = self.parent[i]
            if size < 0:
                sizes.append(-size)
        return sizes

    def groups(self) -> List[List[int]]:
        '全連結成分のサイズの内容のリストを取得'
        '計算量: O(N・α(N))'
        'なんでACLはO(N)でできるんでしょうね'
        groups = dict()
        for i in range(self.n):
            p = self.root(i)
            if not groups.get(p):
                groups[p] = []
            groups[p].append(i)
        return list(groups.values())


n = int(input())
sx, sy, tx, ty = map(int, input().split())
a=[list(map(int,input().split())) for i in range(n)]

uf=UnionFind(n)
circle = []
sn = -1
tn = -1
for i in range(n):
    xi, yi, ri = a[i]
    if (xi - sx) * (xi - sx) + (yi - sy) * (yi - sy) == ri * ri:
        idx1 = i
    if (xi - tx) * (xi - tx) + (yi - ty) * (yi - ty) == ri * ri:
        idx2 = i
    for j in range(i + 1, n):
        xj, yj, rj = a[j]
        if xi == xj and yi == yj and ri != rj:
            continue
        if (xi - xj) * (xi - xj) + (yi - yj) * (yi - yj) <= (ri + rj) * (ri + rj):
            uf.unite(i, j)
if uf.is_same(idx1, idx2):
    print('Yes')
else:
    print('No')
