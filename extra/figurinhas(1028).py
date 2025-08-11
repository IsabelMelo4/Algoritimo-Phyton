def figurinhas(fig1, fig2):
    if fig2 == 0:
        return fig1
    return figurinhas(fig2, fig1 % fig2)

teste = int(input())

for _ in range(teste):
    f1, f2 = map(int, input().split())
    print(figurinhas(f1, f2))
