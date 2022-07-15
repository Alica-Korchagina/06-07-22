import sqlite3

d = {
    5: ['майор', "прапорщик","сержант","cтаршина","cержант","танк"],
    7: ['студент', 'универ', 'колледж',"экзамена","училище","экзамен","профессор"],
    8: ['вpач',"доктор","аптека","лекарство","клиника"],
    4: ['муж','жена','молодожены'],
    9: ['мужик','мужчина'],
    10: ['француз','народов','хохол','кавказец'],
    11: ['менты','наркотик'],
    12: ['новый русский','новых русских'],
    13: ['Вовочка','Вовочке',' (В)овочку'],
    14:['антивирусные','файлы','компьютер','Фотошоп','курсор'],
    15: ['комментатор','футбольная','плывет','кубок','бьют'],
    16: ['Меншиков','граф','Пушкина','князь'],
    17: ['иностранец','кризиса','стране'],
    18: ['автомобиль','скорость','водила','машина','дальнобойщик','гаишники'],
    19: ['собаку','зоопарка','животные','грызуны','котики'],
    20: ['негр', 'сдох', 'Гитлер', 'феминистки'],
    21: ['сказочные герои','Иван-Царевич','Царь-батюшка','золотую рыбку'],
    22: ['Абрам','Еврейская','Моня','еврей'],
    23: ['коррупции','свидетель','грабитель','уголовная статья'],
    24: ['Поручику Ржевскому','Поручик Ржевский','Поручик','Ржевский'],
    25: ['женщины','женщина'],
    26: ['Штирлиц'],
    27: ['ВОВ','Ооо',''],
    28: ['Василий Иваныч','Петька','Шерлоку Холмсу','Холмс'],
    29: ['алкаша','пьете','пьяный'],
    30: ['чукча','чукчу','чукчи'],
    31: ['Обявление','о б я в л е н и е'],
    33: ['дочка','портфель','школы','сын'],
    34: ['программист','баги','Из жизни программистов'],
    35: ['Володя Путин','Путин','Президента Путина','Путина'],
    36: ['тюрьма','заключённый'],#?
    37: ['судом','Судья','подсудимый','судья'],
    38: ['сисадмин'],
    39: ['Кремль','Госдума','Янукович','Верховной Радой'],
    40: ['товарищ','друзья','друг','подруга'],
    41: ['Windows','Билла Гейтса','Билл Гейтс'],
    42: ['теща','тещу','теще','зять'],
    43: ['деньги','рубль','зарабатывать'],
    44: ['режиссер','артистов','актер','Филипп Киркоров'],
    45: ['учитель','урок','теорема','теорему']
}

def category(text):
    for cat in d:
        keywords = d[cat]
        for keyword in keywords:
            if keyword in text:
                connection = sqlite3.connect("anek.db")
                cursor = connection.cursor()
                text_insert = f'''INSERT INTO anek
                                (id,category, anekdot)
                                VALUES
                                (15.07,{cat} , "{text}");'''
                cursor.execute(text_insert)
                connection.commit()
                cursor.close()
                return cat

text = '''Поручику Ржевскому прислали бомбу, он ее открывает, а она не взрывается, думает: 'Емае, как так?!' посмотрел в нее и умер'''
print(category(text))




