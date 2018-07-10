def seq_longest(list_in):
    '''
Longest Consecutive Sequence
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
For example, Given [100, 4, 200, 1, 3, 2], The longest consecutive elements sequence is [1,
2, 3, 4]. Return its length: 4.
Your algorithm should run in O(n) complexity.
如果允许O(nlogn)复杂度，可以先排序，此题不行
但输入中元素无序，考虑用字典（元素为key，value为bool存在性），对每个key左右扩张，直到不连续
    '''
    dict_in = {}
    for i_l in list_in:
        dict_in[i_l] = 'Y'
    list_seq_max = []
    for (i_d,value_d) in dict_in.items():
        list_seq = []
        i_left = 1
        i_right = 1
        while dict_in.get(i_d - i_left) == 'Y':
            i_left += 1
        i_left -= 1
        while dict_in.get(i_d + i_right) == 'Y':
            i_right += 1
        for i_key in range(i_left,i_right+1):
            list_seq.append(i_key)
        if len(list_seq) > len(list_seq_max):
            list_seq_max = list_seq
    return list_seq_max

if __name__ == '__main__':
    dista = [1,2,3,4,5]
    listb = seq_longest(dista)
    print(listb)
    print(len(listb))
        
        
