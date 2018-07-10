'''
给一个数列，其中两个数的和等于目标值，返回索引，并以1为首
'''

class solution:



    def find_index(self,list_in,sum_tar):#时间复杂度高
        inx_max = len(list_in)-1
        for inx_left in range(inx_max):
            inx_right = inx_left + 1
            sum_2 = list_in[inx_left] + list_in[inx_right]
            while(sum_2 != sum_tar and inx_right<inx_max-1):
                inx_right = inx_right +1
                sum_2 = list_in[inx_left] + list_in[inx_right]
            if inx_right == inx_max-1:
                continue
            else:
                return [inx_left+1,inx_right+1]


    def find_inx_2(self,list_in,sum_tar):
        ele_dict = {}
        for ele_inx,ele_list in enumerate(list_in):
            ele_dict[ele_list] = ele_inx+1

        for ele_list in list_in:
            if sum_tar-ele_list in ele_dict:
                return [ele_dict[ele_list],ele_dict[sum_tar-ele_list]]
            



if __name__ == '__main__':
    solu=solution()
    list_in = [1,2,7,4,9]
    tar =9
    res=solu.find_inx_2(list_in,tar)
    print(res)
