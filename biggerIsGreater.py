def findPivot(value, array, type='min'):
    pivot = -1
    for i, v in enumerate(array):
        if type == 'max' and value > v:
            pivot = i
            break
        elif type == 'min' and value < v:
            pivot = i
    return pivot


def findMinStr(array):
    if len(array) == 1:
        return array
    pivot = -1
    for i, v in enumerate(array):
        pivot = findPivot(v, array[i+1:])
        if pivot != -1:
            pivot = pivot + i + 1
            array[pivot], array[i] = array[i], array[pivot]
            break
    if pivot != -1:
        s = findMinStr(array[:-1])
        s.append(array[-1])
        return s
    else:
        return array


def biggerIsGreater(w):
    origin = [ord(v) for _, v in enumerate(w)]
    origin.reverse()
    pivot = 0
    for i, v in enumerate(origin):
        pivot = findPivot(v, origin[i+1:], 'max')
        if pivot != -1:
            pivot = pivot + i + 1
            origin[pivot], origin[i] = origin[i], origin[pivot]
            break
    tmp = origin.copy()
    tmp.reverse()
    earlyStop = ''.join([chr(v) for _, v in enumerate(tmp)])
    if earlyStop == w:
        return 'no answer'
    s = findMinStr(origin[:pivot])
    s.extend(origin[pivot:])
    s.reverse()
    result = ''.join([chr(v) for _, v in enumerate(s)])
    if result == w:
        return 'no answer'
    else:
        return result


def main():
    results = []
    total = 0

    with open('./testBiggerIsGreater.txt', "r") as f:
        for _, line in enumerate(f):
            w = line.rstrip("\n")
            results.append(biggerIsGreater(w))
    
    with open('./resultBiggerIsGreater.txt', "r") as f:
        for count, line in enumerate(f):
            r = line.rstrip("\n")
            if r != results[count]:
                total += 1
                print(r, results[count])
    print(total)

if __name__ == '__main__':
    main()
