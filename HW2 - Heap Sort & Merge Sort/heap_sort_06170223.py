class Solution(object):  
    def heapsort(self, list):

            def heapify(list, len, a):
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

            for a in range(l_len-1, -1, -1):
                sure = list[0]
                list[0] = list[a]
                list[a] = sure
                heapify(list, a, 0)
                if a ==1:
                    break
            
            
            return list   
    
