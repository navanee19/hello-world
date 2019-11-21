arr = [ 2, 3, 4, 10, 40 ] 
value = 40

start = 0
end = len(arr)-1

while start <= end:

    mid = start + (end - start)//2;
    
    if arr[mid] == value:
        print("Element is present")
        break

    elif arr[mid] < value:
        start = mid +1

    else:
        end = mid-1


