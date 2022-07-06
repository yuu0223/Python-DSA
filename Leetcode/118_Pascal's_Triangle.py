class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        self.numRows = numRows
        
        total_list = [[1]]
        
        if self.numRows == 1:
            return total_list
        
        else:
            total_list.append([1,1])
            
            if self.numRows == 2:
                return total_list
            
            else:
                while len(total_list) < self.numRows:
                    total_list.append([])
                
                for a in range(3,self.numRows+1,1):
                    for b in range(1,a+1,1):
                        total_list[a-1].append(1)
                
                for i in range(2,self.numRows,1):
                    for j in range(1,i,1):
                        add_num = total_list[i-1][j-1]+total_list[i-1][j]
                        total_list[i][j] = add_num
                
                return total_list
