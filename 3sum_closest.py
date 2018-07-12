'''
给一个数组，一个目标值，对数组中三个数字求和
返回和与目标的最小距离(或者这个和)
'''

class solution():
    def __init__(self,list_in):
        self.list=sorted(list_in)

    def find_closest(self,target):

        delta_min = target
        sum_min = target*3

        for inx_left in range(len(self.list)-2):
            inx_mid = inx_left +1
            inx_right = len(self.list)-1

            while(inx_mid<inx_right):
                sum_cur = self.list[inx_left]+self.list[inx_mid]+self.list[inx_right]
                if sum_cur < target:
                    delta_cur = target - sum_cur
                    inx_mid = inx_mid+1
                elif sum_cur > target:
                    delta_cur = sum_cur-target
                    inx_right = inx_right -1
                else:
                    return 0
                delta_min = min(delta_min,delta_cur)
                if delta_min== delta_cur:
                    sum_min = sum_cur
        return [delta_min,sum_min]


if __name__=='__main__':
    list_in = [-1,2,1,-4]
    tar =1
    solu = solution(list_in)
    print(solu.find_closest(tar))
                
                    
        
