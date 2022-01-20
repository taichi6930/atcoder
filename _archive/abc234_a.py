
def ftt(t):
    return t ** 2 + 2 * t + 3


def main():
    t = int(input())
    ft = ftt(t)
    ft_t = ft + t
    fft_t = ftt(ft_t)
    fft = ftt(ft)
    ans = ftt(fft_t + fft)
    print(ans)


if __name__ == '__main__':
    main()
