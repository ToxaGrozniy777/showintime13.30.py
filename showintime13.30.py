from tkinter import *
import os

birthday = dict()


def clear():
    input_fulldate.delete(0, END)
    input_month.delete(0, END)
    input_day.delete(0, END)
    input_year.delete(0, END)



def add():
   date = input_fulldate.get()
    if birthday in fulldate:
        label_info.config(text="Такая дата уже существует")
    else:
        value = list()
        value.append(input_month.get())
        value.append(input_day.get())
        value.append(input_year.get())
        birthday[date] = value

        list_birthday.insert(END, date)


def select_list_birthday(event):
    w = event.widget
    i = int(w.curselection()[0])
    date = w.get(i)

    value = birthday[date]
    month = value[0]
    day = value[1]
    year = value[2]


    clear()
    input_tel.insert(0, tel)
    input_month.insert(0, month)
    input_day.insert(0, day)
    input_year.insert(0, year)



window = Tk()
window.title("BirthdayBook")
window.geometry("500x250")

# Объявление элементов окна
label_fulldate = Label(text="Полная дата рождения")
input_date = Entry()

label_month = Label(text="Месяц")
input_month = Entry()

label_day = Label(text="День")
input_day = Entry()

label_year = Label(text="Год")
input_year = Entry()

button_add = Button(text="Добавить", command=add)
button_clear = Button(text="Очистить", command=clear)

label_list_birthdayfulldate = Label(text="Список телефонов")
list_birthdayfulldate = Listbox()

label_info = Label(text="Программа готова к работе")

# Позиционирование
label_fulldate.grid(row=0, column=0, padx=10, pady=5, sticky="w")
input_fulldate.grid(row=0, column=1)

label_month.grid(row=1, column=0, padx=10, pady=5, sticky="w")
input_month.grid(row=1, column=1, padx=10)

label_day.grid(row=2, column=0, padx=10, pady=5, sticky="w")
input_day.grid(row=2, column=1)

label_year.grid(row=3, column=0, padx=10, pady=5, sticky="w")
input_year.grid(row=3, column=1, padx=10)

button_add.grid(row=1, column=2, padx=10)
button_clear.grid(row=3, column=2, padx=10)

label_list_fulldate.grid(row=0, column=3)
list_fulldate.grid(row=1, column=3, rowspan=4, pady=15)

label_info.grid(row=5, column=0, columnspan=4, sticky="w")

list_fulldate.bind('<<ListboxSelect>>', select_list_fulldate)

if os.path.exists("PhoneBook.csv"):
    with open("PhoneBook.csv", "r") as file:
        lines = file.readlines()
        for line in lines:
            elements = line.split(";")
            tel = elements[0]
            last_name = elements[1]
            first_name = elements[2]
            patronymic = elements[3]
            address = elements[4]
            value = list()
            value.append(last_name)
            value.append(first_name)
            value.append(patronymic)
            value.append(address)
            phone_book[tel] = value
            list_tel.insert(END, tel)

window.mainloop()