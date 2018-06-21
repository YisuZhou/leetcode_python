def find_kth(list_sorted_1,list_sorted_2,k):
    '''
给定两个已经排好序（升序）的数组，找到两种所有元素中第K大的元素
    '''
    count_k = 0
    index_1 = 0
    index_2 = 0
    
    while(count_k < k and index_1 <= len(list_sorted_1)-1 and index_2 <= len(list_sorted_2)-1):
        if (len(list_sorted_1)+len(list_sorted_2)<k):
            print("总元素不足k个")
        if list_sorted_1[index_1] == list_sorted_2[index_2]:
            count_k +=2
            if count_k >=k:
                return list_sorted_1[index_1]
            else:
                index_1 +=1
                index_2 +=1
        if list_sorted_1[index_1] > list_sorted_2[index_2]:
            count_k +=1
            if count_k >= k:
                return list_sorted_2[index_2]
            else:
                index_2 +=1
        if list_sorted_1[index_1] < list_sorted_2[index_2]:
            count_k +=1
            if count_k >= k:
                return list_sorted_1[index_1]
            else:
                index_1 +=1


if __name__ == '__main__':
    lista = [2,3,4,5]
    listb = [4,5]
    k = 3
    print(find_kth(lista,listb,k))
    
