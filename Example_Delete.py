from clsChess import Chess

# создать объект базы данных
database_Chess = Chess()


# удаление по id спортсема
def delete_command(id):
    database_Chess.delete(id)
    print(f"Данные спортсмена  с id = {id} удалены")


# просмотр всех записей
def view_command():
    for row in database_Chess.view():
        print(row)


# основная программа
print("Список спортсменов")
view_command()

id_delete = int(input("Введите id спортсменов "))
delete_command(id_delete)

print("Список спортсменов")
view_command()
