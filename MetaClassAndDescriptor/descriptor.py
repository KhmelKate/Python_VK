class Integer:
    
    def __init__(self, name):
        self.name = name  
        self.val = 0
        
    def __get__(self, instance, owner):
        return self.val
    
    def __set__(self, instance, value):
        if isinstance(value, int):
            self.val = value
        else: 
            raise ValueError('Only int.')  
        
        
class String:
    
    def __init__(self, name):
        self.name = name  
        self.val = ''
        
    def __get__(self, instance, owner):
        return self.val
    
    def __set__(self, instance, value):
        if isinstance(value, str) and len(value) <= 20:
            self.val = value
        else:  
            raise ValueError('Only string. Lenght must be lower or equal than 20')
            

class PositiveInteger:
    
    def __init__(self, name):
        self.name = name  
        self.val = 0
        
    def __get__(self, instance, owner):
        return self.val
    
    def __set__(self, instance, value):
        if isinstance(value, int) and value > 0:
            self.val = value
        else:    
            raise ValueError('Only positiv int.')
          
        

class Data:
    num = Integer('num')
    name = String('name')
    price = PositiveInteger('price')
