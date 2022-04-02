def dfs(u, used, order):
    used[u] = True
    for v in adj_list[u]:
        if not used[v]:
            dfs(v, used, order)
    order.append(u)


n, m = map(int, input().split())
adj_list = [set() for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u].add(v)
    adj_list[v].add(u)

used = [False] * n
order = []
for u in range(n):
    if not used[u]:
        dfs(u, used, order)
print(order[::-1])
