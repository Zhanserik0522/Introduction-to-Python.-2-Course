# Step 1

range(10)
range(0, 10)
range(0, 10, 5)

# Step 2
print("Step 2")
for i in range(10):
    print(i, end="")

# Step 3
print("Step 3")
for i in range(10):
    print(i**2, end="")

print()
weekdays = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

for day in weekdays:
    print('Сегодня {}'.format(day))

# Step 4
print("Step 4")
direct_revenue = [83171,151604, 46315, 98753, 208648, 184682, 204061,134911,94791,109076,37254, 224991,36400,149320, 171336, 83854, 206799,180922, 235647, 217546, 200478, 239445, 144901, 26522,177971,148458,154937,196095,140202,189223]
week_1_revenue = direct_revenue[:7]

# Step 5
print("Step 5")
total_revenue = 0
for day in week_1_revenue:
    total_revenue += day
print(total_revenue)

# Step 6
print("Step 6")
total_revenue = 0
for day in week_1_revenue:
   total_revenue += day
   print('Значение element - {}, сумма на текущий момент - {}'.format(day, total_revenue))

# Проверочное задание 1
minValue = 4
maxValue = 18
my_list = []
for i in range(minValue, maxValue + 1, 2):
    my_list += [i]
for i in range(len(my_list)):
    print(my_list[i] ** 0.5)
# Какое значение будет предпоследним? - 4.0

# Step 7
print("Step 7")
queriesList = "смотреть сериалы онлайн".split( '   ' )
print(queriesList)

# Проверочное задание 2

queriesText = 'смотреть сериалы онлайн;новости спорта;афиша кино;курс доллара;сериалы этим летом;курс по питону;сериалы про спорт'
sum_of_words = 1
for i in range(len(queriesText)):
    if queriesText[i] == ";":
        sum_of_words += 1

print(sum_of_words)

# Блок 7. Проверки
print("Блок 7. Проверки")

a = 5
if  a == 5:
    print('Результат вычислений корректный')

VK_visit = 1500
VK_order = 14
FB_visit = 2200
FB_order = 17
if VK_order / VK_visit > FB_order / FB_visit:
    print("Конверсия ВКонтакте выше")
else:
    print("Конверсия Facebook выше")

# Шаг 2. Проверка нескольких условий одновременно
source = ['прямой заход','яндекс','партнерка','вконтакте','инфопартнер']

a = 1
b = 2
if a == 1 and b == 2:
    print('Оба условия a=1 и b=2 выполнены одновременно')
else:
    print('Хотя бы одно из условий не выполнено')

if a == 1 or b == 2:
    print('Хотя бы одно из условий a=1 и b=2 выполнено')
else:
    print('Ни одно из условий a=1 и b=2 не выполнено')

if source == 'прямой переход' or source == 'инфопартнер':
    print('Это бесплатный переход')
else:
    print('Это платный переход')

# Шаг 3. Проверки в списках
list_of_strings = ['Москва', 'Новосибирск', 'Воронеж', 'Краснодар', 'Иркутск']
string_to_find = 'Краснодар'

if string_to_find in list_of_strings:
    print("{} содержится в списке городов".format(string_to_find))
else:
    print("Город {} не из списка".format(string_to_find))

semantic_list = ['одеяло !купить', 'одеяло !продажа','одеяло цена',  'одеяло стоимость','одеяло прайс','одеяло дешево', 'одеяло недорого','одеяло заказать','одеяло на заказ', 'одеяло с доставкой', 'одеяло магазин','одеяло интернет магазин', 'одеяло со скидкой','одеяло акция','одеяло распродажа']
string_to_find = 'одеяло по дешевке'
if string_to_find in semantic_list:
     print('Фраза "{}" входит в семантическое ядро' .format( string_to_find))
else:
     print('Фраза "{}" не входит в семантическое ядро' .format( string_to_find))

# Шаг 4. Проверка наличия набора слов
# ПРОВЕРКА НАЛИЧИЯ НАБОРА СЛОВ

text = 'Название языка питон произошло вовсе не от вида пресмыкающихся. Автор назвал язык в честь популярного британского комедийного телешоу 1970-х Летающий цирк Монти Пайтона'
words_to_find = ['питон', 'Монти', 'проверка', 'честь', 'шоу', 'драма']

for ans in words_to_find:
    if ans in text:
        print(ans, end=" ")

queries = "смотреть сериалы онлайн,новости спорта,афиша кино,курс доллара,сериалы этим летом,курс по питону,сериалы про спорт"
words = ['сериалы', 'курс']

query_list = queries.split(',')
filtered_queries = []

for query in query_list:
    if any(word in query for word in words):
        filtered_queries.append(query)

result = ','.join(filtered_queries)

print(result)