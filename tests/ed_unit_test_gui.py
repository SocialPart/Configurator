import unittest
from unittest.mock import patch
import tkinter as tk
from tests.ed_test_gui import MainWindow  # Импортируем наш класс для тестов

class TestMainWindow(unittest.TestCase):

    @patch('tkinter.filedialog.askopenfilename')  # Мокаем диалоговое окно
    @patch('tkinter.messagebox.showinfo')         # Мокаем вывод сообщений
    @patch('tkinter.messagebox.showwarning')      # Мокаем вывод предупреждений
    def test_select_archive_file_chosen(self, mock_warning, mock_info, mock_file_dialog):
        # Настраиваем возвращаемое значение мока для функции filedialog.askopenfilename
        mock_file_dialog.return_value = 'test_archive.zip'

        # Создаем экземпляр нашего приложения
        app = MainWindow()

        # Вызываем тестируемую функцию
        app.select_archive()

        # Проверяем, что был вызван правильный messagebox (с информацией)
        mock_info.assert_called_with("Файл выбран", "Вы выбрали test_archive.zip")
        mock_warning.assert_not_called()  # Проверяем, что предупреждение не вызывалось

    @patch('tkinter.filedialog.askopenfilename')  # Мокаем диалоговое окно
    @patch('tkinter.messagebox.showinfo')         # Мокаем вывод сообщений
    @patch('tkinter.messagebox.showwarning')      # Мокаем вывод предупреждений
    def test_select_archive_no_file_chosen(self, mock_warning, mock_info, mock_file_dialog):
        # Настраиваем возвращаемое значение мока для функции filedialog.askopenfilename
        mock_file_dialog.return_value = ''  # Пользователь не выбрал файл

        # Создаем экземпляр нашего приложения
        app = MainWindow()

        # Вызываем тестируемую функцию
        app.select_archive()

        # Проверяем, что было вызвано предупреждение
        mock_warning.assert_called_with("Нет файла", "Вы не выбрали файл")
        mock_info.assert_not_called()  # Проверяем, что messagebox.showinfo не вызывался

if __name__ == '__main__':
    unittest.main()
