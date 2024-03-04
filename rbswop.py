def binarySearch( arr, ele, index=0):
    if len( arr) == 1 and arr[ 0] != ele:
        return
    elif ele in arr:
        mid = len( arr) // 2
        if arr[ mid] == ele:
            index += mid
            return index
        elif arr[ mid] > ele:
            return binarySearch( arr[:mid], ele, index)
        elif arr[ mid] < ele:
            index += mid
            return binarySearch( arr[mid:], ele, index)
    else:
        return