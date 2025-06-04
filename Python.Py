import tkinter as tk
from tkinter import messagebox, simpledialog
from collections import Counter

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Универсальная программа")
        self.geometry("600x500")
        
        self.create_main_menu()
    
    def create_main_menu(self):
        self.clear_window()
        
        tk.Label(self, text="Выберите задание:", font=('Arial', 14)).pack(pady=20)
        
        buttons = [
            ("Форматирование строк", self.string_formatting),
            ("Проверка четности числа", self.check_even_odd),
            ("Проверка возраста", self.check_age),
            ("Подсчет цифр в числе", self.count_digits),
            ("Возведение в степень", self.power_calculation),
            ("Преобразование словаря", self.dict_transformation),
            ("Пересечение списков", self.list_intersection),
            ("Подсчет слов", self.word_count),
            ("Выход", self.quit)
        ]
        
        for text, command in buttons:
            tk.Button(self, text=text, width=25, command=command).pack(pady=5)
    
    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()
    
    def back_to_menu(self):
        self.create_main_menu()
    
    def show_result(self, result_text):
        result_window = tk.Toplevel(self)
        result_window.title("Результат")
        tk.Label(result_window, text=result_text, justify=tk.LEFT, padx=20, pady=20).pack()
        tk.Button(result_window, text="Закрыть", command=result_window.destroy).pack(pady=10)

    def string_formatting(self):
        self.clear_window()
        
        tk.Label(self, text="Форматирование строк", font=('Arial', 14)).pack(pady=10)
        
        tk.Label(self, text="Имя:").pack()
        name_entry = tk.Entry(self)
        name_entry.pack()
        
        tk.Label(self, text="Фамилия:").pack()
        surname_entry = tk.Entry(self)
        surname_entry.pack()
        
        tk.Label(self, text="Возраст:").pack()
        age_entry = tk.Entry(self)
        age_entry.pack()
        
        def show_result():
            name = name_entry.get()
            surname = surname_entry.get()
            age = age_entry.get()
            
            if not (name and surname and age):
                messagebox.showerror("Ошибка", "Все поля должны быть заполнены!")
                return
            
            format_str = "Ваше имя: {}, Фамилия: {}, Возраст: {} лет".format(name, surname, age)
            f_str = f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет"
            
            result_text = f"Реализация через format:\n{format_str}\n\nРеализация через f-string:\n{f_str}"
            self.show_result(result_text)
        
        tk.Button(self, text="Показать результат", command=show_result).pack(pady=10)
        tk.Button(self, text="Назад", command=self.back_to_menu).pack()
    
    def check_even_odd(self):
        self.clear_window()
        
        tk.Label(self, text="Проверка четности числа", font=('Arial', 14)).pack(pady=10)
        
        tk.Label(self, text="Введите число:").pack()
        number_entry = tk.Entry(self)
        number_entry.pack()
        
        def check_number():
            num_str = number_entry.get()
            
            if not num_str.lstrip('-').isdigit():
                messagebox.showerror("Ошибка", "Введено не число!")
                return
            
            num = int(num_str)
            if num < 0:
                messagebox.showerror("Ошибка", "Число должно быть положительным!")
                return
            
            result = "четным" if num % 2 == 0 else "нечетным"
            self.show_result(f"Число {num} является {result}")
        
        tk.Button(self, text="Проверить", command=check_number).pack(pady=10)
        tk.Button(self, text="Назад", command=self.back_to_menu).pack()
    
    def check_age(self):
        self.clear_window()
        
        tk.Label(self, text="Проверка возраста", font=('Arial', 14)).pack(pady=10)
        
        tk.Label(self, text="Введите ваш возраст:").pack()
        age_entry = tk.Entry(self)
        age_entry.pack()
        
        def verify_age():
            age_str = age_entry.get()
            
            if not age_str.isdigit():
                messagebox.showerror("Ошибка", "Введено не число!")
                return
            
            age = int(age_str)
            if age < 0:
                messagebox.showerror("Ошибка", "Возраст не может быть отрицательным!")
                return
            
            status = "совершеннолетний" if age >= 18 else "несовершеннолетний"
            self.show_result(f"Вы {status}.")
        
        tk.Button(self, text="Проверить", command=verify_age).pack(pady=10)
        tk.Button(self, text="Назад", command=self.back_to_menu).pack()
    
    def count_digits(self):
        self.clear_window()
        
        tk.Label(self, text="Подсчет цифр в числе", font=('Arial', 14)).pack(pady=10)
        
        tk.Label(self, text="Введите число (или 'exit' для выхода):").pack()
        number_entry = tk.Entry(self)
        number_entry.pack()
        
        def count():
            num_str = number_entry.get()
            
            if num_str.lower() == 'exit':
                self.back_to_menu()
                return
            
            if not num_str.lstrip('-').isdigit():
                messagebox.showerror("Ошибка", "Данные не являются числом!")
                return
            
            num_digits = len(num_str.lstrip('-'))
            self.show_result(f"В этом числе {num_digits} цифры.")
        
        tk.Button(self, text="Подсчитать", command=count).pack(pady=10)
        tk.Button(self, text="Назад", command=self.back_to_menu).pack()
    
    def power_calculation(self):
        self.clear_window()
        
        tk.Label(self, text="Возведение в степень", font=('Arial', 14)).pack(pady=10)
        
        tk.Label(self, text="Введите числа через пробел:").pack()
        numbers_entry = tk.Entry(self, width=50)
        numbers_entry.pack()
        
        tk.Label(self, text="Введите степень:").pack()
        power_entry = tk.Entry(self)
        power_entry.pack()
        
        def calculate_power():
            try:
                items = numbers_entry.get().split()
                power = int(power_entry.get())
                
                result = []
                for item in items:
                    if item.lstrip('-').isdigit():
                        result.append(str(int(item) ** power))
                    else:
                        result.append(item * power)
                
                self.show_result("Результат: " + " ".join(result))
            except ValueError:
                messagebox.showerror("Ошибка", "Некорректный ввод!")
        
        tk.Button(self, text="Вычислить", command=calculate_power).pack(pady=10)
        tk.Button(self, text="Назад", command=self.back_to_menu).pack()
    
    def dict_transformation(self):
        self.clear_window()
        
        tk.Label(self, text="Преобразование словаря", font=('Arial', 14)).pack(pady=10)
        
        dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}
        
        keys = set(dct.keys())
        values = set(dct.values())
        union = keys.union(values)
        
        result = (f"Исходный словарь: {dct}\n\n"
                 f"Множество ключей: {keys}\n"
                 f"Множество значений: {values}\n"
                 f"Объединение множеств: {union}")
        
        self.show_result(result)
        tk.Button(self, text="Назад", command=self.back_to_menu).pack()
    
    def list_intersection(self):
        self.clear_window()
        
        tk.Label(self, text="Пересечение списков", font=('Arial', 14)).pack(pady=10)
        
        tk.Label(self, text="Введите первый список чисел через пробел:").pack()
        list1_entry = tk.Entry(self, width=50)
        list1_entry.pack()
        
        tk.Label(self, text="Введите второй список чисел через пробел:").pack()
        list2_entry = tk.Entry(self, width=50)
        list2_entry.pack()
        
        def find_intersection():
            try:
                list1 = set(map(int, list1_entry.get().split()))
                list2 = set(map(int, list2_entry.get().split()))
                
                intersection = list1 & list2
                result = "Общие элементы: " + " ".join(map(str, intersection))
                self.show_result(result)
            except ValueError:
                messagebox.showerror("Ошибка", "Некорректный ввод чисел!")
        
        tk.Button(self, text="Найти пересечение", command=find_intersection).pack(pady=10)
        tk.Button(self, text="Назад", command=self.back_to_menu).pack()
    
    def word_count(self):
        self.clear_window()
        
        tk.Label(self, text="Подсчет слов в строке", font=('Arial', 14)).pack(pady=10)
        
        tk.Label(self, text="Введите строку:").pack()
        text_entry = tk.Entry(self, width=50)
        text_entry.pack()
        
        def count_words():
            """Подсчитывает количество слов"""
            text = text_entry.get().lower()
            words = text.split()
            
            if not words:
                messagebox.showerror("Ошибка", "Строка пустая!")
                return
            
            word_counts = Counter(words)
            result = "\n".join([f"{word}: {count}" for word, count in word_counts.items()])
            self.show_result(result)
        
        tk.Button(self, text="Подсчитать", command=count_words).pack(pady=10)
        tk.Button(self, text="Назад", command=self.back_to_menu).pack()

if __name__ == "__main__":
    app = Application()
    app.mainloop()