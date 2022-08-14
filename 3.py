# КлассTomato:
# 1. Создайте классTomato
# 2. Создайте статическое свойствоstates, которое будет содержать все стадии
# созревания помидора
# 3. Создайте метод__init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и2) _state - принимает первое
# значение из словаряstates
# 4. Создайте методgrow(), который будет переводить томат на следующую стадию
# созревания
# 5. Создайте методis_ripe(), который будет проверять, что томат созрел(достиг
# последней стадии созревания)
# КлассTomatoBush
# 1. Создайте классTomatoBush
# 2. Определите метод__init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса
# Tomato. Данный список будет храниться внутри динамического свойстваtomatoes.
# 3. Создайте методgrow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
# 4. Создайте методall_are_ripe(), который будет возвращать True, если все томаты из
# списка стали спелыми
# 5. Создайте методgive_away_all(), который будет чистить список томатов после
# сбора урожая
# КлассGardener
# 1. Создайте классGardener
# 2. Создайте метод__init__(), внутри которого будут определены два динамических
# свойства: 1) name - передается параметром, является публичным и2) _plant -принимает объект классаTomato,
# являетсяprotected
# 3. Создайте методwork(), который заставляет садовника работать, что позволяет
# растению становиться более зрелым
# 4. Создайте методharvest(), который проверяет, все ли плоды созрели. Если все-садовник собирает урожай.
# Если нет- метод печатает предупреждение.
# 5. Создайте статический методknowledge_base(), который выведет в консоль справку
# по садоводству.
# Тесты:
# 1. Вызовите справку по садоводству
# 2. Создайте объекты классовTomatoBush иGardener
# 3. Используя объект классаGardener, поухаживайте за кустом с помидорами
# 4. Попробуйте собрать  урожай
# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 6. Соберите урожай


class Tomato:
    states={1:'начало',2:'спеет',3:'созрел'}

    def __init__(self,index,status=states[1]):
        self._index=index
        self._states=status

    def grow(self,i):
        if i<3:
            self._index = i+1
            self._states=Tomato.states[i+1]
            return self._states
        self._states = Tomato.states[i]
        return self._states

    def is_ripe(self):
        if self._index==3:
            return 'томат созрел(достиг последней стадии созревания)'
        return 'томат не созрел'


class TomatoBush(Tomato):
    def __init__(self,kol:int):
        self.spisok_tomato = []
        for i in range(kol):
            self.spisok_tomato.append(Tomato(i)._states)

    def tomatoes(self):
        return self.spisok_tomato

    def grow_all(self):
        self.new_spisok_tomato=[]
        for j in self.spisok_tomato:
            for k in Tomato.states.items():
                if j==k[1]:
                    key=k[0]+1
                    if key>3:
                        self.new_spisok_tomato.append(Tomato.states[j])
                    else:
                        self.new_spisok_tomato.append(Tomato.states[key])
        self.spisok_tomato=self.new_spisok_tomato
        return self.spisok_tomato

    def ll_are_ripe(self):
        counter=0
        for l in range (len(self.spisok_tomato)):
            if self.spisok_tomato[l]=='созрел':
                counter+=1
            if counter==len(self.spisok_tomato):
                return True
        return False

    def give_away_all(self,text=''):
        if text=='сбор урожая':
            self.spisok_tomato.clear()
        return self.spisok_tomato

class Gardener(TomatoBush):
    def __init__(self,name='',_plant=''):
        self.name=name
        self._plant=_plant

    def work(self,ix):
        Tomato(ix).grow(ix)


    def harvest(self):
        s=TomatoBush(2).ll_are_ripe()
        if s==False:
            print('плоды не созрели!')
        else:
            TomatoBush().give_away_all('сбор урожая')

def main():
    t = Tomato(1)
    print(t._index, t._states)
    print(t.grow(1))
    print(t.is_ripe())

    tb=TomatoBush(2)
    print(tb.tomatoes())
    print(tb.grow_all())
    print(tb.ll_are_ripe())
    print(tb.give_away_all('сбор урожая'))

    grd=Gardener('Вася')
    print(grd.work(1))
    print(grd.harvest())



main()