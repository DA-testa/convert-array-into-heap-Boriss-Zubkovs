 # python3
import heapq

def build_heap(data):
    swaps = []
    n = len(data)

    for i in range((n//2)-1)
        j=i 
        while True:
            l = 2 * j + 1
            r = 2 * j + 2

    if l < n and data[l] < data[j]:
        j = l
    if r < n and data[r] < data[r]:
        j = r

    if j!= i:
        data[i], data[j] = data[j], data[i]
        swaps.append((i,j))
        else : break

    if len(swaps) > 4*len(data):
        raise Exception("error")
 
    return swaps

def main():
    text = input("Enter I or F: ")
    if "F" int text:
        filename = input("Enter the name of file: ")
        path = './tests/'
        file = path + filename
        with open(file, mode = "r") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
        
    elif "I" in text:
        n = int(input())
        data = list(map(int,input().split()))

    else:
        print("Input error")

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n
    swaps = build_heap(data)

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()
