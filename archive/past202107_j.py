import copy
import collections
import sys


def dfs(i, UV, c=None):
    if len(c) != 0:
        if collections.Counter(c).most_common()[0][1] > 1:
            print("Yes")
            sys.exit()

    c.append(i)

    for a in c:
        if a not in UV:
            UV[a] = {}
        if a != i:
            UV[a].add(i)

    if i not in UV:
        return
    lis = list(UV[i])
    for j in list(lis):
        dfs(j, UV=UV, c=copy.copy(c))
    return


def main():
    n, m = map(int, input().split())
    UV = {}
    st = collections.deque()
    for i in range(m):
        u, v = map(int, input().split())
        st.append(u)
        if u not in UV:
            UV[u] = set()
        UV[u].add(v)

    for i in list(st):
        dfs(i, UV=UV, c=[])
    print("No")


if __name__ == '__main__':
    main()
