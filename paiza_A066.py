n = int(input())
work_lis = sorted(sorted([tuple(map(int, input().split()))
                  for _ in range(n)], key=lambda x: x[1]), key=lambda x: x[0])

(st, gl) = work_lis[0]
ans = gl - st + 1

for i, (st_a, gl_a) in enumerate(work_lis):
    if st_a > gl + 1:
        ans = max(gl - st + 1, ans)
        st = st_a
        gl = gl_a
        continue
    gl = max(gl_a, gl)

print(max(gl - st + 1, ans))
