def timeToWords(h, m):
    time = ''
    noRule = {'0': 'o\' clock', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
              '8': 'eight', '9': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve', '20': 'twenty', '15': 'quarter', '30': 'half'}
    print(noRule.has_key(str(h)))
    print(noRule.has_key(str(m)))
    if m > 30:
        to = 60-m
        if noRule.has_key(str(to)):
            time += noRule[str(to)] + ' minutes to '
        else:
            to /= 10
            if to == 1:
                time += noRule[str(to)] + 'teen minutes to '
            else:
                tmp = (60-m) % 10
                time += 'twenty ' + noRule[str(tmp)] + ' minutes to '
    else:
        if noRule.has_key(str(m)):
            time += noRule[str(to)] + ' past '
        else:
            to /= 10
            if to == 1:
                time += noRule[str(to)] + 'teen minutes past '
            else:
                tmp = m % 10
                time += 'twenty '+noRule[str(tmp)] + ' minutes past '

    if roRule.has_key(str(h)):
        time += noRule[str(h)]
    print(time)

def main():
    timeToWords(5, 30)


if __name__ == 'main':
    main()
