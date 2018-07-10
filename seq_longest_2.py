class solution:

    def __init__(self):
        self.len_map={}


    def find_longest(self,list_in):
        if len(list_in)==0:
            return 0
        len_longest = 1
        for ele_in in list_in:
            if ele_in in self.len_map:#避免重复元素检测，浪费时间
                continue
            self.len_map[ele_in] =1 
            if ele_in-1 in self.len_map:
                l_new = self.len_merge(ele_in-1)
                len_longest = max(len_longest,l_new)
            if ele_in+1 in self.len_map:
                l_new = self.len_merge(ele_in)
                len_longest = max(len_longest,l_new)
        return len_longest
                
                 


    def len_merge(self,ele_in):
        left = ele_in 
        right = ele_in +1
        ele_low = left - self.len_map[left] +1
        ele_up = right + self.len_map[right] -1
        len_longest = ele_up - ele_low + 1
        self.len_map[ele_low] = len_longest
        self.len_map[ele_up] = len_longest
        return len_longest


if __name__ =='__main__':
    solu=solution()
    list_in = [1,3,5,2,4,6,10,12]
    print(solu.find_longest(list_in))
        
