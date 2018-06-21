def find_kth(list_sorted_1,list_sorted_2,k):
    '''
假设两个数组的元素都大于k/2个，每次比较能够删掉一半，类似二分查找，
再次强调，有序的数组的查找，最先考虑二分
    '''
    m = len(list_sorted_1)
    n = len(list_sorted_2)
    
    if(m+n < k):
        print("总元素数不足k个")
        exit(0)
    if (m==0):
        return list_sorted_2[k-1]
    if (n==0):
        return list_sorted_1[k-1]
    if (k==1):
        return min(list_sorted_1[0],list_sorted_2[0])
    
    index_1 = min(k//2,m)
    index_2 = k - index_1

    if (list_sorted_1[index_1-1]<list_sorted_2[index_2-1]):#1的前index个一定在前k个里面
        return find_kth(list_sorted_1[index_1:],list_sorted_2,k-index_1)
    elif (list_sorted_1[index_1-1]>list_sorted_2[index_2-1]):#2的前index个一定在前k个里面
        return find_kth(list_sorted_1,list_sorted_2[index_2:],k-index_2)
    else:#相等的话随便哪个
        return list_sorted_1[index_1-1]
        
    
    


if __name__ == '__main__':
    lista=[2,3,4]
    listb=[1,5,6,7]
    k=5
    if(len(lista)<=len(listb)):
        print(find_kth(lista,listb,k))
    else:
        print(find_kth(listb,lista,k))
    
