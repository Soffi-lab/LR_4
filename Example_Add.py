from clsChess import Chess

# создать объект базы данных
database_Chess = Chess()


# логика
# добавление записи
def add_command(id, lastname_s, Date_of_Birth, country, sports_category, Name , the_date_of_the, busy_place):
    (id, lastname_s, Date_of_Birth, country, sports_category, Name , the_date_of_the, busy_place)


# просмотр всех записей
def view_command():
    for row in database_Chess.view():
        print(row)


# основная программа в консоли
# добавление записи
for i in range(5):
    add_command(input("Фамилия спортсмена:"),
                    float(input("дата рождения:")),
                    input("Название страны:"),
                    float(input("спортивный разряд:")),
                    input("Название турнира:"),
                    float(input("дата проведения:")),
                    float(input("занятое место:")))
# просмотр всех записей
view_command()
