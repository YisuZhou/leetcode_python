def remove_dup(list_sorted):
    '''
Follow up for ”Remove Duplicates”: What if duplicates are allowed at most twice?
For example, Given sorted array A = [1,1,1,2,2,3],
Your function should return length = 5, and A is now [1,1,2,2,3]
    '''
    index = 2
    allow_dup = 2#可拓展
    for i in list_sorted[2:]:
        if list_sorted[index-allow_dup] != i :         
            list_sorted[index] = i
            index +=1
    return [list_sorted[:index],index]

if __name__ == '__main__':
    list1=[1,1,1,2,2,3]
    result_list = remove_dup(list1)
    print("结果是：",result_list[0])
    print("长度是：",result_list[1])
        
        
