'''
给一个数列，其中三个数之和等于目标值
输出所有组合，不需要索引了

（先排序，再夹逼）
'''


class solution():
    def __init__(self,list_in):
        self.result = []
        self.sort_list(list_in)

    def sort_list(self,list_in):
        list_in.sort()

    def find_3sum(self,list_in,target):

        #用left带头
        for inx_left in range(len(list_in)-2):
            inx_mid = inx_left+1
            inx_right = len(list_in)-1
        #先动mid,再动right
            while inx_mid<inx_right:#注意下面，一次只能动一下的不能用while！
                if list_in[inx_left]+list_in[inx_mid]+list_in[inx_right] < target : 
                    inx_mid = inx_mid +1
                    while(list_in[inx_mid]==list_in[inx_mid-1] and inx_mid<inx_right):
                        inx_mid = inx_mid +1#注意一旦动了inx就要判断是不是符合大要求，mid<right
                elif list_in[inx_left]+list_in[inx_mid]+list_in[inx_right] > target :
                    inx_right = inx_right -1
                    while (list_in[inx_right]==list_in[inx_right+1] and inx_mid<inx_right):
                        inx_right = inx_right -1
                else:
                    if [list_in[inx_left],list_in[inx_mid],list_in[inx_right]] not in self.result:
                        self.result.append([list_in[inx_left],list_in[inx_mid],list_in[inx_right]])
                    inx_mid = inx_mid +1
                    inx_right = inx_right -1

        return self.result


if __name__ =='__main__':

    list_in = [-1,0,1,2,-1,-4]
    tar = 0
    solu=solution(list_in)
    print(solu.find_3sum(list_in,tar))
    

                    
                    
                    
            
        

