class Solution(object):  
    def heapsort(self, list):

            def heapify(list, len, a):
                #重複步驟後，heapify只會做最前面三項(0,1,2)的排序
                largest = a
                left = 2*a+1
                right = 2*a+2
        
                if left < len and list[largest] < list[left] :
                    largest = left

                if  right < len and list[largest] < list[right]:
                    largest = right

                if largest != a:
                    swap = list[a]   #建一個swap寄放母項
                    list[a] = list[largest]  #將較大的子項成為母項 大的換上去
                    list[largest] = swap  #將寄放在swap的母項成為子項 小的換下來
                    heapify(list, len, largest) #換過的largest已成為2a或2a+1項，繼續heapify下面的元素
        
            l_len = len(list)

            for a in range((l_len//2)-1, -1, -1):
                heapify(list, l_len, a)
                #由下往上3個3個做heapify
                #假如有7項，那就會從第2項開始heapify

            for a in range(l_len-1, -1, -1):
                sure = list[0]
                list[0] = list[a]
                list[a] = sure
                heapify(list, a, 0)
                #若a=1的時候(只剩一個元素)就會停止
       
            return list   
    

    #Reference: https://exceptionnotfound.net/heap-sort-csharp-the-sorting-algorithm-family-reunion/
