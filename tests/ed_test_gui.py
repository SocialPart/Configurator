import tkinter as tk
from tkinter import filedialog, messagebox

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("XML Archive Parser")

        # Кнопка для выбора архива
        self.choose_button = tk.Button(self.root, text="Выбрать архив", command=self.select_archive)
        self.choose_button.pack(pady=20)

    def select_archive(self):
        # Открываем диалог для выбора файла
        archive_path = filedialog.askopenfilename(title="Выберите архив", filetypes=[("ZIP files", "*.zip")])
        if archive_path:
            messagebox.showinfo("Файл выбран", f"Вы выбрали {archive_path}")
        else:
            messagebox.showwarning("Нет файла", "Вы не выбрали файл")

    def run(self):
        self.root.mainloop()

# Запуск GUI
if __name__ == "__main__":
    app = MainWindow()
    app.run()