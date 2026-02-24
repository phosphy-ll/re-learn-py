class Jar:
    material = "Glass" #Это атрибут класса, он для всех кто ссылается на этот класс один и тот же, т.е obj & obj2, хотя прописан он единожны
    def __init__(self, inside, numbers, water_lvl): 
        self.inside = inside #Атрибут обьекта это перемменые внутри класса, то есть inside, атрибут присваивается при self.a = a, ну вот
        self.numbers = numbers
        self.water_lvl = water_lvl

        #Уровень воды и закрепленных значений
        if not isinstance(water_lvl, (int, float)):
            raise TypeError("water lvl must be a num")
        if water_lvl < 0 or water_lvl > MAX_WATER:
            raise ValueError(f"water_lvl wust be beetwen 0 - {MAX_WATER}")
    def __str__(self): # ну тут и так написано, но обьясню для себя чтоб запомнить, в целом чтоб была красивая строка, и можно было вызвать чисто print(obj) а не ебатся там
        """красивый вывод для print(obj)"""
        return (
            f"Jar(material= {self.material}, inside= {self.inside}, "
            f"number of= {self.numbers}, water = {self.water_lvl}ml, "
            f"status of jar = {self.status()}, " #тут нужен () тк мы вызываем не сам метод а его результат

            )
    def start(self):
        print("Jar is opening...")
    #тут пишется типа доливка
    def fill(self, amount):
        """Fill water: (amount in ml).""" #защита от отриц знач
        if amount < 0:
            raise ValueError("amount must be +")
        if not self.inside:
            return amount
        old = self.water_lvl
        new = old + amount
        if new > MAX_WATER:
            overflow = new - MAX_WATER
            self.water_lvl = MAX_WATER
            return overflow #выдача значений перелива
        self.water_lvl = new
        return 0

    def pour(self, amount): # отлив воды
        if amount < 0: # так же защита от отриц знач
            raise ValueError("amount must be +")
        old = self.water_lvl
        new = old - amount
        if new < 0:
            underflow = abs(new)
            self.water_lvl = 0 #возврат лишн значений
            return underflow
        self.water_lvl = new
        return 0
    
    def ri(self, item): #удаляет обьект
         if item in self.inside:
             self.inside.remove(item)
             return True
         return False #ну тут впринципе все легко и понятно, удаление обьекта в целом из внутрянки, можно и не из нее, удаление выборочное, O(n)
    
    def adi(self, item): #добавление обьекта в конец списка
        if item in self.inside:
            return False
        self.inside.append(item) #ну добавление в конец списка чтоб не нагружать, O(1)
        return True

    def status(self): #статус банки в целом, типо пустая или нет и тд
        if self.water_lvl == 0:
            return "Jar is empty"
        if self.water_lvl == MAX_WATER:
            return "Jar is full"
        MAX_WATER = 1000 # выставление макс значения воды, удобно тем что можно поменять тут и в целом поменяется везде
        percent = (self.water_lvl / MAX_WATER) * 100
        return f"Partially filled ({percent}%)" 
        

obj1 = Jar(["pickles", "garlic"], [1, 2, 3], 882) # ну тут сами банки с внутрянкой
obj2 = Jar(["empty"], [0], 0)
obj3 = Jar([], [], 0)
obj2.inside.pop() #по сути своей удобая штучка, но ток для листов и чтоб с конца удалять, если удалять не с конца то занимает O(n)
obj2.inside.append("Nuttela") #тоже добавление, в целом как и поп, больше нечего сказать
obj2.fill(732) # вызов метода fill, то же самое и с пуром но он мне нах не нужен
obj1.ri("pickles") # вызов удаления выборочного, remove удаляет по "названию", ну короче да
obj3.adi("onion") # добавление
(obj1.start( )) # вызов метода старт
print(obj1) 
print(obj2)
print(obj3)
