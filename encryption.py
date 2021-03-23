import math


def encryption(msg):
    msg = msg.replace(' ', '')
    rows = math.floor(math.sqrt(len(msg)))
    cols = math.ceil(math.sqrt(len(msg)))
    if rows*cols < len(msg):
        rows = cols
    encrypt = ''
    for i in range(cols):
        for j in range(rows):
            if j*cols+i > len(msg)-1:
                break
            encrypt += msg[j*cols+i]
        if i+1 < cols:
            encrypt += ' '
    return encrypt


def main():
    msg = 'iffactsdontfittotheorychangethefacts'
    print(encryption(msg))


if __name__ == '__main__':
    main()
