def search(list_rotated,target):
    '''
Follow up for ”Search in Rotated Sorted Array”: What if duplicates are allowed?
Would this affect the run-time complexity? How and why?
Write a function to determine if a given target is in the array.
这两个题目最重要的地方是：首先要判断哪一段是单调的
上一题，不允许重复，则如果list[m]>=list[n],则[n,m]为递增
这一题，允许重复，则list[m]>list[n],则[n,m]为递增，等于的时候就不一定，需要n+1看一下
    '''
    first = 0
    last = len(list_rotated)-1
    while(first != last):
        mid = (first + last)//2
        if list_rotated[mid] == target:
            return mid
        if list_rotated[first] < list_rotated[mid]:
            if (list_rotated[first]<=target and target<list_rotated[mid]):
                last = mid
            else:
                first = mid+1
        if list_rotated[first] > list_rotated[mid]:
            if (list_rotated[mid]<target and target<=list_rotated[last]):
                first = mid+1
            else:
                last = mid
        else:
            first +=1
    return -1

if __name__ =='__main__':
    list1=[1,3,1,1,1]
    t=1
    print(search(list1,t))


























                
    
        
