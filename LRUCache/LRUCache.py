class LRUCache:
    
    def __init__(self, limit=42):
        self.limit = limit
        self.LRUCache_list = []
        self.LRUCache_dict = {}
        
    def set(self, key, value):
        # Добавление нового элемента или изменение значения старого
        if key in self.LRUCache_list:
            self.change_position(key)
            self.LRUCache_dict[key] = value
        else:
            if len(self.LRUCache_list) < self.limit:
                self.append_new_value(key, value)
            else:
                self.remove_last_key()
                self.append_new_value(key, value)
            
    def append_new_value(self, key, value):
        # Добавление нового элемента
        self.LRUCache_list.insert(0, key)
        self.LRUCache_dict[key] = value
        
    def remove_last_key(self):
        # Удаление ключа, который давно не использовался
        last_key = self.LRUCache_list.pop(-1)
        self.LRUCache_dict.pop(last_key)
        
    def change_position(self, key):
        # Изменение позиции ключа в листе LRUCache_list
        self.LRUCache_list.remove(key)
        self.LRUCache_list.insert(0, key)
        
    def get(self, key):
        # Получение элемента
        if key not in self.LRUCache_list:
            return None
        else:
            self.change_position(key)
            return self.LRUCache_dict[key]
