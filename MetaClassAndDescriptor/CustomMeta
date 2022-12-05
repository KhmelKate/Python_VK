class CustomMeta(type):
    
    def __new__(cls, name, base, attr):
        new_attr = {}
        for key, val in attr.items():
            if key.startswith('__') and key.endswith('__'):
                new_attr[key] = val
            else:
                new_attr['custom_' + key] = val
        
        print(new_attr)
        return type(name, base, new_attr)

    
    
class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"
