'''
把数组中指定元素删掉，就地删掉，不占用其他空间
'''

class solution():
    def __init__(self,list_in):
        self.list=list_in
    def remove_ele(self,target):
        while target in self.list:
            self.list.remove(target)
        return self.list

if __name__=='__main__':
    list_in = [1,2,3,4,5,5,6,2,3,2]
    tar = 2
    solu = solution(list_in)
    print(solu.remove_ele(tar))
