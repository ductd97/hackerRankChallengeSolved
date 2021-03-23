def extraLongfatorials(n):
    if(n == 1):
        return 1
    return n*extraLongfatorials(n-1)
def main():
    print("Function")
    print(extraLongfatorials(45))
if __name__== "__main__":
    main()