import os
import csv
from termcolor import colored

files_directory = r'C:\Users\IT\Desktop\Архив'
print('читаем файлы из', files_directory)
files_names = os.listdir(files_directory)
print('В директории найдены файлы:', *files_names)

headers_template = {
    'id': 0,
    'name': 1,
    'surname': 2,
    'age': 3,
    'height': 4,
    'weight': 5,
    'eyesight': 6,
    'education': 7,
    'english_language': 8
}

colors = ['green', 'magenta', 'blue', 'yellow', 'cyan', 'red', 'white', 'green', 'magenta']

for file_name in files_names:
    file_path = os.path.join(files_directory, file_name)
    if not file_name.endswith('.csv'):
        continue
    with open(file_path, 'r', encoding='UTF-8') as file:
        reader = csv.reader(file, delimiter='#')
        headings = next(reader)

        if not all(field in headings for field in headers_template):
            print(f'Файл {file_name} содержит неверные заголовки')
            continue

        print(f'Работаем с файлом: {colored(file_name, "cyan")}')
        print()
        print('Читаем данные:')

        for row in reader:
            formatted_data = {}
            for header, idx in headers_template.items():
                idx = headers_template[header]
                value = row[idx] if idx < len(row) else ''
                color = colors[idx]
                formatted_data[header] = colored(f'{header}: {value}', color)


            for header in headers_template:
                print(formatted_data[header], end=' ')

            print()





        #сохранить файл: with open('result.scv'), mode='w', encoding='utf-8') as file:
        #    writer = csv.writer(file, delimiter='#')
        #    writer.writerows(formatted_data)
        # какой элемент ряда к какому заголовку относится
        # меняю порядок в соответствии с шаблоном заголовков
        # добавляем упорядоченный ряд в копилку
