from random import randrange
def merge_sort(arr):
    if (len(arr) <= 1 ): return arr 
    mid = len(arr) // 2
    l = merge_sort(arr[:mid])
    r = merge_sort(arr[mid:])
    i = j = k = 0
    while (i < len(l) and j < len(r)):
        if (l[i] < r[j]):
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1
    while(i < len(l)):
        arr[k] = l[i]
        i+=1
        k+=1
    while(j < len(r)):
        arr[k] = r[j]
        j+=1
        k+=1
    return arr

def main():
    arr =  [ randrange(0,1000) for i in range(20)] 
    print ("Given array is")
    print(arr)
    merge_sort(arr)
    print("Sorted array is: ") 
    print(arr)
        
main()