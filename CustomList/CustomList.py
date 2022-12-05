class CustomList(list):
    
    """Перегрузка оператора вычитание"""
    def __sub__(self, other):
        sub_list = []
        len_self, len_other = len(self), len(other)
        if len_self > len_other:
            for index in range(len_other):
                sub_list.append(self[index]-other[index])
            for index in range(len_self - len_other):
                sub_list.append(self[len_other + index])
        if len_self < len_other:
            for index in range(len_self):
                sub_list.append(other[index] - self[index])
            for index in range(len_other - len_self):
                sub_list.append(-other[len_self + index])   
        if len_self == len_other:
            for index in range(len_other):
                sub_list.append(self[index] - other[index])
        return CustomList(sub_list)
    
    """Перегрузка оператора вычитание"""
    def __rsub__(self, other):
        if isinstance(other, list):
            other = CustomList(other)
            return other.__sub__(self)
        else:
            print('Операция вычитания типа CustomList производится с типами CustomList и list')
            
    """Перегрузка оператора сложения"""        
    def __add__(self, other):
        add_list = []
        len_self, len_other = len(self), len(other)
        if len_self > len_other:
            for index in range(len_other):
                add_list.append(self[index] + other[index])
            for index in range(len_self - len_other):
                add_list.append(self[len_other + index])
        if len_self < len_other:
            for index in range(len_self):
                add_list.append(other[index] + self[index])
            for index in range(len_other - len_self):
                add_list.append(other[len_self + index])
        if len_self == len_other:
            for index in range(len_other):
                add_list.append(self[index] + other[index])
        return CustomList(add_list) 
    
    """Перегрузка оператора сложения"""
    def __radd__(self, other):
        if isinstance(other, list):
            other = CustomList(other)
            return other.__add__(self)
        else:
            print('Операция сложения типа CustomList производится с типами CustomList и list')
            
    """Вычисление суммы элементов"""
    def custom_sum(self):
        sum_of_self = 0
        for value in self:
            sum_of_self += value
        return sum_of_self
            
    
    """Перегрузка оператора =="""
    def __eq__(self, other):
        if isinstance(other, list):
            other = CustomList(other)
        if isinstance(self, list):
            other = CustomList(other)
        return self.custom_sum() == other.custom_sum()
    
    """Перегрузка оператора <"""
    def __lt__(self, other):
        if isinstance(other, list):
            other = CustomList(other)
        if isinstance(self, list):
            other = CustomList(other)
        return self.custom_sum() < other.custom_sum()
    
    """Переопределение функции str"""
    def __str__(self):
        return f'Элементы списка: {super().__str__()}\n' \
                f'Сумма элементов списка: {self.custom_sum()}'
