class Solution():
    def merge_sort(self, list):
        self.list = list
        list1 = []
        list2 = []
        final_list = []
        
        n = len(list)
        
        if n<=1:
            return list
        
        else:
            list1 = list[:n//2]
            list2 = list[(n//2):] 
        #將原始list切割成兩等份
         
        list1 = sorted(list1)
        list2 = sorted(list2)
        #各自先進行排序
            
        def arrange(list1=[],list2=[]):
            
            if list1[0]<list2[0] or list1[0] == list2[0]:
                final_list.append(list1[0])
                list1 = list1.remove(list1[0])
            #若list1的第一個數比list2的第一個數小或兩者相等，則將list1[0]新增至final_list，並從list1中移除
            
            else:
                final_list.append(list2[0])
                list2 = list2.remove(list2[0]) 
            #若list1的第一個數比list2的第一個數大，則將list2[0]新增至final_list，並從list2中移除
        
        while(list1 != [] and list2 !=[]):
            arrange(list1,list2)
        #判斷list1和list2內若還有值就繼續進行arrange，若無值則繼續下面的if-else
        
        if list1!=[]:
            final_list.append(list1[0])
        elif list2!=[]:
            final_list.append(list2[0])
        #將Max值直接新增至final_list的最後(因為已經無從比較)
            
        return final_list
