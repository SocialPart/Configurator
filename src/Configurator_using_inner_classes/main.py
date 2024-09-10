from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tar_prepare as prep


# Получение расположения бэкапа

def open_file():
    filepath = filedialog.askopenfilename()
    prep.open_and_extract(filepath)
    change_page()
    print(filepath)

# Закрытие приложения

def finish():
    prep.deleting_temp_after_close()
    root.destroy()

# Показать страницу

def show_page(page):
    # Скрыть все страницы
    for p in pages.values():
        p.pack_forget()
    # Показать указанную страницу
    pages[page].pack()

def change_page():
    show_page("page2")

root = Tk()
root.protocol("WM_DELETE_WINDOW", finish)
root.title("Aris_Protocol")
root.geometry("650x650")

page1 = Frame(root)
page2 = Frame(root)
Label(page1, text="Начальная страница").pack()
Label(page2, text="Страница с загруженным бэкапом").pack()

pages = {"page1": page1, "page2": page2}
show_page("page1")


#Убираем ненужные пунктиры
root.option_add("*tearOff", FALSE)

main_menu = Menu()
file_menu = Menu()
settings_menu = Menu()

main_menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Открыть бэкап", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=finish)


root.config(menu=main_menu)
root.mainloop()