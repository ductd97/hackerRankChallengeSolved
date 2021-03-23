def recursiveDigitSum(n,k):
    print(n,k)
    if len(str(n))==1:
        return n
    arr = [v for (_,v) in enumerate(str(n))]
    sum = 0;
    for i in range(len(arr)):
        sum +=int(arr[i])
    return recursiveDigitSum(sum*k,1)
def main():
    n=9875
    k=4
    print(recursiveDigitSum(n,k))
if __name__=="__main__":
    main()
