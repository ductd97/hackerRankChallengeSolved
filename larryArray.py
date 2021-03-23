def larrayArray(array):
    for i in range(len(array)):
        if(array.index(i+1) == i+1):
            continue
        else:
            

def main():
    array = [3, 2, 1, 4]
    larrayArray(array)


if __name__ == '__main__':
    main()

