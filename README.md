Задание 1:
Строка содержит пять временных значений. Они записаны через запятую:
`'1h 45m,360s,25m,30m 120s,2h 60s'.`
Напиши цикл, который посчитает общее количество минут. Результат сохрани в переменную и выведи на экран. Используй в решении методы split(), replace() и оператор in.
Обрати внимание: временное значение может состоять из одного, двух или трёх единиц времени. Значения расшифровываются так:
часы — любое положительное целое число и символ h;
минуты — любое положительное целое число и символ m;
секунды — положительное целое число кратное 60 и символ s.

Задание 2:
Исправь класс Tester так, чтобы:
при вызове метода work_hard у экземпляра класса tester_1 печаталось 'tester_1 Можно отдыхать';
при вызове метода work_hard у экземпляра класса tester_2 печаталось 'tester_2 Что ж, ещё часок поработаю!'.
Вызовы менять не нужно.
```class Tester:

    def __init__(name):
        name = name
        deadline = True

    def work_hard(self, deadline=True):
        if self.deadline:
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')

tester_1 = Tester(name='tester_1')
tester_1.work_hard(deadline=False)  # 'tester_1 Можно отдыхать'
tester_2 = Tester(name='tester_2')
tester_2.work_hard(deadline=True)   # 'tester_2 Что ж, ещё часок поработаю!' 
```

Задание 3:
Словарь содержит информацию о чемпионатах по футболу в 21 веке:
год. Например, 1988;
страна, которая выиграла чемпионат мира по футболу. Например, Англия.
Что нужно сделать:
Добавь в словарь 2022 год. В 2022 году чемпионом стала Аргентина.
Выведи на экран всех чемпионов в формате год - страна.
Проверь, выигрывала ли Италия в 21 веке. Есть переменная countryсо значением Италия. Проверь, содержится ли она в словаре. Если да, выведи надпись Италия cтановилась чемпионом мира по футболу в 21 веке!. А если страна отсутствует среди значений словаря, выведи на экран Италия не выигрывала чемпионат мира по футболу в 21 веке.
```
world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

country = 'Италия'
```


Задание 4:
Есть два списка задач. Список new_tasks содержит задачи, которые по плану нужно протестировать до конца месяца. Список completed_tasks — уже завершенные в текущем месяце.
Что нужно сделать:
Тестировщик только что завершил задачу task_005. Перенеси её из списка new_tasks в список completed_tasks. Сделай это в одно действие.
Запрос task_007 заказчик убрал из плана, потому что нужно доработать требования. Удали его из списка new_tasks.
Последней задаче из списка new_tasks заказчик поднял приоритет, поэтому её нужно будет взять в работу следующей. Выведи её на экран.
```
new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006'] 
```
Задание 5
Напиши класс TestCase. Он должен содержать конструктор и методы.
В конструкторе инициализируются поля:
steps — шаги тест-кейса, в качестве параметра принимает пустой словарь;
result — ожидаемый результат выполнения тест-кейса, принимает None в качестве параметра.
Методы:
Метод set_step — добавляет в словарь steps шаг тест-кейса. Принимает два параметра: step_number и step_text. Ключ — это step_number(номер шага), а значение — step_text (текстовое описание шага).
Метод delete_step — удаляет шаг из steps по ключу step_number, который передали в метод.
Метод set_result — устанавливает ожидаемый результат. Он помещает его в атрибут result по параметру result, который передали методу.
Метод get_test_case — печатает информацию о составе тест-кейса в формате {'Шаги': {<номер шага>: '<описание шага>'}, 'Ожидаемый результат': '<вывод ожидаемого результата>'}.

Пример вывода метода get_test_case:
```
{
    'Шаги': {
            1: 'Перейти на сайт', 
            2: 'Перейти в раздел Товары', 
            3: 'Нажать кнопку «В корзину» у первого товара'
    }, 
    'Ожидаемый результат': 'Товар окажется в корзине'
} 
class TestCase:

    def __init__(self):


test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case() 
```
Дополнительные задания

Задание 1:
В словаре types хранятся типы багов. Его ключи — числа от 1 до 5, а значения — от 'Блокирующий'  до 'Тривиальный' соответственно. 
```
types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
} 
```
В словаре tickets хранятся тикеты (задачи), которые заведены на эти баги. Ключи — числовое значение критичности от 1 до 5, а значения — список с тикетами, которые этим значениям критичности соответствуют. Но некоторые тикеты добавлены несколько раз в разные списки.
```
tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
} 
```
Составь итоговый словарь, где ключи — это значение критичности, например, 'Значительный', а значения — списки с уникальными тикетами. 
Для этого напиши две функции: 
одна удаляет дубли из списков с тикетами,
вторая связывает уровень критичности со списком уникальных тикетов.
Если тикет есть в одном списке, то он уже не может быть в списках на уровень ниже. 
Вторая функция принимает на вход два параметра: словарь types с типами багов и словарь tickets со списком багов. Функция возвращает словарь, где уровень критичности связан со списком уникальных тикетов.
Итоговый словарь должен получиться таким:
```
tickets_by_type = {
    'Блокирующий': ['API_45', 'API_76', 'E2E_4'],
    'Критический': ['UI_19', 'API_65', 'E2E_45'],
    'Значительный': ['E2E_2'],
    'Незначительный': ['E2E_9'],
    'Тривиальный': ['API_61']
} 
```
Вызывать функцию необязательно.

Задание 2:
Напиши функцию, которая рассчитывает цифровой корень числа. 
Чтобы получить числовой корень числа, нужно:
Первоначальное число разбить на цифры по разрядам.
Сложить эти цифры.
С суммой сделать то же самое: разбить на цифры и сложить их.
И так — пока не получится одна цифра (от 1 до 9), которая и будет цифровым корнем числа.
Например, числовой корень числа 4851 — 9.
4851 → 4+8+5+1 = 18
18 → 1+8 = 9
Цифровой корень 97569 равен 9:
97569 → 9+7+5+6+9 = 36
36 → 3+6 = 9
Пример посложнее. Для числа 889987 цифровой корень — 4:
889987 → 8+8+9+9+8+7= 49
49 → 4+9 = 13
13 → 4
Функцию можно назвать digit_root(num). Она принимает на вход один параметр — num (число), а возвращает цифровой корень.
Условия: 
входное число натуральное (1, 2, 3, … );
число не превышает 
1
0
7
10 
7
 .
