def permutation(arr, results):
    result = []
    if len(arr) == 1: 
        return arr
    for i in range(len(arr)):
        arr[0], arr[i] = arr[i], arr[0]
        if len(arr[1:]) >= 1:
            tmp = permutation(arr[1:],results)
            tmp.append(arr[0])
            result.extend(tmp)
    print(result)
    return result
def main():
    arr = [1,2,3]
    permutation(arr,[])
if __name__ == "__main__":
    main()