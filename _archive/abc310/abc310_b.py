n, m = map(int, input().split())
PCF = [list(map(int, input().split())) for _ in range(n)]
for i, pcfi in enumerate(PCF):
    pi = pcfi[0]
    fi = pcfi[2:]
    for j, pcfj in enumerate(PCF):
        pj = pcfj[0]
        fj = pcfj[2:]
        if i == j:
            continue
        if pi < pj:
            continue
        swi = False
        for f in fi:
            if f not in fj:
                swi = True
                break
        if swi:
            continue
        if pi > pj:
            exit(print("Yes"))
        for f in fj:
            if f not in fi:
                exit(print("Yes"))
exit(print("No"))
