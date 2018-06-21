def remove_dup(list_sorted):
    '''
    Remove Duplicates from Sorted Array

    Given a sorted array, remove the duplicates in place such that each element appear only once
    and return the new length.
    Do not allocate extra space for another array, you must do this in place with constant memory.
    For example, Given input array A = [1,1,2],
    Your function should return length = 2, and A is now [1,2].
    因为是已经排好序的，所以从前面开始直接覆盖就没问题。
    '''
    index = 0
    for i in list_sorted:
        if list_sorted[index] != i:
            index +=1#注意要先加1，否则会把前面的覆盖掉，而且python里面没有++
            list_sorted[index] = i            
    return [list_sorted,index+1]#注意要加1

def remove_dup_1(list_sorted):
    return set(list_sorted)
        
    
if __name__ == '__main__':
    list1=[1,1,2]
'''
    result_list = remove_dup_1(list1)
    print(result_list)
    print(len(result_list))
'''    
'''
    result_list = remove_dup(list1)
    print("最后的数组是：",result_list[0][0:result_list[1]])
    print("不重复的个数是：",result_list[1])
'''
    



