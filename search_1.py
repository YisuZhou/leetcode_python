def search(list_rotated,target):
    '''
 Search in Rotated Sorted Array
 Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
    有序数列查找，首先想到二分
    '''
    len_list = len(list_rotated)
    first = 0
    last = len_list-1
    if first==last:
        return first
    while first != last:
        mid = (first+last)//2
        if list_rotated[mid] == target:
            return mid
        if list_rotated[mid]>= list_rotated[first]:
            if (list_rotated[first]<target and target<list_rotated[mid]):
                last = mid
            else:
                first = mid+1
        else:
            if (list_rotated[mid]<target and target<=list_rotated[last]):
                first = mid+1
            else:
                last = mid
    return -1


if __name__ =='__main__':
    list1=[4]
    t=4
    print(search(list1,t))














                
        
        
