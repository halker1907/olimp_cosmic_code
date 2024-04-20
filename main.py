import os
import csv

# files_directory = input("Выберете ваш путь к файлам")
files_directory = r'C:\Users\IT\Desktop\Архив'

print('читаем файлы из', files_directory)
files_names = os.listdir(files_directory)
print('Вдиректории найдены файлы:', *files_names)

files_name = [
    file_name for file_name in files_names if file_name.endswith('.csv')
]

print('Работаем с файлами:', *files_names)

headers_template = [
        'id',
        'name',
        'surname',
        'age',
        'height',
        'weight',
        'eyesight',
        'education',
        'english_language'
    ]

for file_name in files_names:
    file_path = os.path.join(files_directory, file_name)
    with open(file_path, 'r', encoding='UTF-8') as file:
        reader = csv.reader(file, delimiter='#')
        headings = next(reader)
        if not all(field in headings for field in headers_template):
            print(f'Файл {file_name} содержит неверные заголовки')

        # Читаем ряды со 2-го
        # какой элемент ряда к какому заголовку к какому заголовку относится
        # меняю порядок в соответствии с шаблоном заголовков
        # добавляем упорядоченный ряд в копилку
