def nonDevisibleSubset(s, n, k):
    posSum = {}
    maxLen = 0
    subList = []
    for i in range(0, n):
        posSub = [s[i]]
        for j in range(0, n):
            if i == j:
                continue
            first_cond = (s[i] + s[j]) % k
            if first_cond != 0:
                canInsert = True
                for l in range(0, len(posSub)):
                    second_cond = (s[j] + posSub[l]) % k
                    if second_cond == 0:
                        canInsert = False
                        break
                if canInsert:
                    posSub.append(s[j])
        if len(posSub)>maxLen:
            maxLen = len(posSub)
            subList = posSub
    return maxLen
def main():
    s = [770528134, 663501748, 384261537, 800309024, 103668401,
         538539662, 385488901, 101262949, 557792122, 46058493]
    nonDevisibleSubset(s, len(s), 5)


if __name__ == '__main__':
    main()
# 4 8 7 4 1 2 1 9 2 3
