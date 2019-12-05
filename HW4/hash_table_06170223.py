from Cryptodome.Hash import MD5 as md5

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None
            
class MyHashSet:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        
        
    def md5(self, val): #將輸入的值加密
        
        new = md5.new()
        new.update(val.encode('utf-8'))
        finish = new.hexdigest()
        return finish
        
    def ascii_sum(self, val): #將輸入的值轉為數字
        
        ascii_word = []
        total_sum = 0
        
        for i in val:
            trans = ord(i)
            ascii_word.append(trans)
       
        b =len(ascii_word)-1
        
        for a in ascii_word:
            sum_word = a*(10**b)
            total_sum = total_sum+sum_word
            b=b-1
        
        return total_sum
        
    
    def mod(self, val): #將輸入之值取mod，並放進哪個位置
        
        number = self.ascii_sum(val)
        mod = number%self.capacity
        
        return mod
        
        
    def add(self, key):
        
        mod_key = self.mod(key)
        md5_key = self.md5(key)
        
        if self.data[mod_key] == None:
            dict = {}
            self.data[mod_key] = dict
            self.data[mod_key][key] = md5_key 
            
        else:
            self.data[mod_key][key] = md5_key
    
    
    
    def remove(self, key):
        
        mod_key = self.mod(key)
        md5_key = self.md5(key)
        
        if self.data[mod_key] == None:
            return 
            
        else:
            self.data[mod_key].pop(key)
            
        
    
    
    def contains(self, key):
        
        mod_key = self.mod(key)
        md5_key = self.md5(key)
        
        if self.data[mod_key] != None:
            if key in self.data[mod_key]:
                return True
            
            else:
                return False
            
        else:
            return False
   

#Reference:
#https://www.itread01.com/content/1541137210.html
#https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/
#http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html
