from functools import reduce
from transliterate import translit

names = 'Алиса, Александра, Алёна, Алина, Алла, Анастасия, Анжелика, Анна, Валентина, Валерия, Вера, Вероника, ' \
        'Виктория, Галина, Дарья, Диана, Ева, Евгения, Екатерина, Алёна, Елена, Елизавета, Жанна, Инна, Ирина, ' \
        'Карина, Кристина, Ксения, Лариса, Людмила, Маргарита, Марина, Мария, Мила, Милана, Надежда, ' \
        'Наталья, Ника, Нина, Оксана, Олеся, Ольга, Полина, Руслана, Сания, Светлана, София, Софья, Тамара, Татьяна, ' \
        'Юлия, Яна, Александр, Алексей, Анатолий, Андрей, Антон, Аркадий, Арсений, Артём, Артур, Борис, Вадим, ' \
        'Валентин, Валерий, Василий, Виктор, Виталий, Владимир, Владислав, Вячеслав, Георгий, Глеб, Григорий, ' \
        'Даниил, Денис, Дмитрий, Евгений, Егор, Иван, Игорь, Илья, Кирилл, Константин, Лев, Леонид, Максим, Марк, ' \
        'Матвей, Михаил, Николай, Олег, Павел, Пётр, Роман, Руслан, Сергей, Степан, Тимур, Фёдор, Юрий, ' \
        'Ярослав'

transliterated_names = list(map(lambda s: s.strip().replace("'", ""), translit(names, reversed=True)
                                .split(', ')))

last_names = '''Смирнов
    Иванов
    Кузнецов
    Соколов
    Попов
    Лебедев
    Козлов
    Новиков
    Морозов
    Петров
    Волков
    Соловьёв
    Васильев
    Зайцев
    Павлов
    Семёнов
    Голубев
    Виноградов
    Богданов
    Воробьёв
    Фёдоров
    Михайлов
    Беляев
    Тарасов
    Белов
    Комаров
    Орлов
    Киселёв
    Макаров
    Андреев
    Ковалёв
    Ильин
    Гусев
    Титов
    Кузьмин
    Кудрявцев
    Баранов
    Куликов
    Алексеев
    Степанов
    Яковлев
    Сорокин
    Сергеев
    Романов
    Захаров
    Борисов
    Королёв
    Герасимов
    Пономарёв
    Григорьев
    Лазарев
    Медведев
    Ершов
    Никитин
    Соболев
    Рябов
    Поляков
    Цветков
    Данилов
    Жуков
    Фролов
    Журавлёв
    Николаев
    Крылов
    Максимов
    Сидоров
    Осипов
    Белоусов
    Федотов
    Дорофеев
    Егоров
    Матвеев
    Бобров
    Дмитриев
    Калинин
    Анисимов
    Петухов
    Антонов
    Тимофеев
    Никифоров
    Веселов
    Филиппов
    Марков
    Большаков
    Суханов
    Миронов
    Ширяев
    Александров
    Коновалов
    Шестаков
    Казаков
    Ефимов
    Денисов
    Громов
    Фомин
    Давыдов
    Мельников
    Щербаков
    Блинов
    Колесников
    Карпов
    Афанасьев
    Власов
    Маслов
    Исаков
    Тихонов
    Аксёнов
    Гаврилов
    Родионов
    Котов
    Горбунов
    Кудряшов
    Быков
    Зуев
    Третьяков
    Савельев
    Панов
    Рыбаков
    Суворов
    Абрамов
    Воронов
    Мухин
    Архипов
    Трофимов
    Мартынов
    Емельянов
    Горшков
    Чернов
    Овчинников
    Селезнёв
    Панфилов
    Копылов
    Михеев
    Галкин
    Назаров
    Лобанов
    Лукин
    Беляков
    Потапов
    Некрасов
    Хохлов
    Жданов
    Наумов
    Шилов
    Воронцов
    Ермаков
    Дроздов
    Игнатьев
    Савин
    Логинов
    Сафонов
    Капустин
    Кириллов
    Моисеев
    Елисеев
    Кошелев
    Костин
    Горбачёв
    Орехов
    Ефремов
    Исаев
    Евдокимов
    Калашников
    Кабанов
    Носков
    Юдин
    Кулагин
    Лапин
    Прохоров
    Нестеров
    Харитонов
    Агафонов
    Муравьёв
    Ларионов
    Федосеев
    Зимин
    Пахомов
    Шубин
    Игнатов
    Филатов
    Крюков
    Рогов
    Кулаков
    Терентьев
    Молчанов
    Владимиров
    Артемьев
    Гурьев
    Зиновьев
    Гришин
    Кононов
    Дементьев
    Ситников
    Симонов
    Мишин
    Фадеев
    Комиссаров
    Мамонтов
    Носов
    Гуляев
    Шаров
    Устинов
    Вишняков
    Евсеев
    Лаврентьев
    Брагин
    Константинов
    Корнилов
    Авдеев
    Зыков
    Бирюков
    Шарапов
    Никонов
    Щукин
    Дьячков
    Одинцов
    Сазонов
    Якушев
    Красильников
    Гордеев
    Самойлов
    Князев
    Беспалов
    Уваров
    Шашков
    Бобылёв
    Доронин
    Белозёров
    Рожков
    Самсонов
    Мясников
    Лихачёв
    Буров
    Сысоев
    Фомичёв
    Русаков
    Стрелков
    Гущин
    Тетерин
    Колобов
    Субботин
    Фокин
    Блохин
    Селиверстов
    Пестов
    Кондратьев
    Силин
    Меркушев
    Лыткин
    Туров'''

transliterated_last_names = list(map(lambda s: s.strip().replace("'", "''"), translit(last_names, reversed=True)
                                     .split('\n')))

# print(transliterated_names)
# print(transliterated_last_names)
