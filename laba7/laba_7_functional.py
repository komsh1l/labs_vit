import psycopg2
import datetime


def connect_to_db(a, b):
    """
    Возвращает все указанные данные, где id в [a,b]
    Пр. вывода: (4, 'Понедельник', 'Игровые виды спорта', 'Практика', 'в А-С/Зал', '15:25-17:00', 'Волохова С.В.')
    """
    conn = psycopg2.connect(database="vvit_laba_7",
                            user="postgres",
                            password="bed8w7",
                            host="localhost",
                            port="5432")
    cursor = conn.cursor()

    cursor.execute(f"""select tt.id, tt.day, s.name, tt.view, tt.room, tt.start_time, t.full_name
                from subject s, teacher t, timetable tt
                where s.id=t.fk_id_subject and t.id=tt.fk_id_teacher and tt.id between {a} and {b} order by tt.id;""")

    data_bd = cursor.fetchall()
    cursor.close()
    conn.close()

    return data_bd


def week_number():
    """возвращает номер текущей недели"""
    number = datetime.datetime.now().isocalendar()[1] - 4
    return number


def date_output(date):
    """
    Преобразует дату
    Пр. входных данных: 2023-04-26 18:55:25.087953
    Вывод: ['ср', '26', 'апр.']
    """
    months = {1: 'янв.', 2: 'февр.', 3: 'марта', 4: 'апр.', 5: 'мая', 6: 'июня.', 7: 'июля', 8: 'авг.', 9: 'сент.',
              10: 'окт.', 11: 'нояб.', 12: 'дек.'}
    weekdays = {0: "пн", 1: "вт", 2: "ср", 3: "чт", 4: "пт", 5: "сб", 6: "вс"}
    now_date = date.strftime('%d-%m').split('-')
    number_day = str(int(now_date[0]))
    day = weekdays[date.weekday()]
    month = months[int(now_date[1])]

    return [day, number_day, month]


def title_output(title, flag=False):
    """
    Возращает строку следующего вида:

    ''РАСПИСАНИЕ НА {название}
    БВТ2204 • {текущая дата}
    {номер недели}, {тип недели}''

    Если флаг Тру, то добавляется строка:
    ''Отображено расписание {название}
    {номер след. недели}, {тип недели}''
    """
    data = date_output(datetime.datetime.today())
    view_week = ['нижняя', 'верхняя']

    template = f"""РАСПИСАНИЕ НА {title}
БВТ2204 • {data[0]}, {data[1]} {data[2]}
№{week_number()}, {view_week[week_number() % 2]}"""
    if flag:
        template += f"\nОтображено расписание на следующую неделю\n(№{week_number() + 1}, {view_week[abs(week_number() % 2 - 1)]})"

    return template


def day_out(a, b, number_for_date=0):
    """
    Возвращает строку с рассписанием на заданный промежуток времени
    """
    data = connect_to_db(a, b)
    day_text = ""
    weekdaysmapping = {'Понедельник': 0, 'Вторник': 1,
                       'Среда': 2, 'Четверг': 3, 'Пятница': 4, 'Суббота': 5}
    now_time = datetime.datetime.today().weekday()
    for i in range(b - a + 1):
        if i % 5 == 0:
            data_time = date_output(datetime.date.today() - datetime.timedelta(
                days=now_time - number_for_date - weekdaysmapping[data[i][1]]))
            day = "\n\n" + data[i][1] + " - " + data_time[1] + " " + data_time[2]
            day_text += day
        num = str(i % 5 + 1) + ". "
        start_time = data[i][5]
        subject = data[i][2]
        view = data[i][3]
        room_number = data[i][4]
        teacher = data[i][6]

        if subject == "<Нет пары>":
            day_text += "\n" + num + start_time + "\n" + subject + "\n"
        else:
            day_text += "\n" + num + start_time + "\n" + subject + "\n" + view + " " + room_number + "\n" + teacher + "\n"
    day_text += "\nЛабораторная работа №7, создание тг. бота"
    return day_text


def schedule(a):
    """
    Здесь происходит первоначальная настройка, указываются id для запроса к бд,
    передаются нужные параметры другим функциям.
    функция возвращает склеенную строку из двух строк, которые возвращают функции title_output() и day_out()
    """
    days = ['Понедельник', 'Вторник', 'Среду', 'Четверг', 'Пятницу', 'Субботу']
    if week_number() % 2 == 1:
        n = 0
    else:
        n = 30
    if a == 6:
        return title_output("НЕДЕЛЮ") + day_out(1 + n, 30 + n)
    elif a == 7:
        return title_output("СДЕДУЮЩУЮ НЕДЕЛЮ", flag=True) + day_out(1 + 30 - n, 30 + 30 - n, number_for_date=7)
    else:
        return title_output(days[a].upper()) + day_out(a * 5 + 1 + n, a * 5 + 5 + n)


hello = '''Я учебный бот, созданный, чтобы показывать расписание группы БВТ2204,
я использую базу данных postgres, могу вывести ссылку на оф. сайт МТУСИ,
а также показать какая сегодня неделя: верхняя или нижняя.

Список команд:
/monday - Расписание на Понедельник
/tuesday - Расписание на Вторник
/wednesday - Расписание на Среду
/thursday - Расписание на Четверг
/friday - Расписание на Пятницу
/saturday - Расписание на Субботу
/nowweek - Расписание на неделю
/nextweek - Расписание на следующую неделю
/week - Показывает какая сейчас неделя
/help - Рассказывает информацию о себе
/mtuci – Выводит ссылку на оф. сайт Мтуси 

Если не хотите прописывать команды вручную, нажмите на кнопку меню и выберите нужную команду. 
'''


