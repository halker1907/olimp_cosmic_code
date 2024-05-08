import os    
import csv    
from termcolor import colored    
    
files_directory = r'C:\Users\IT\Desktop\Архив'    
print('читаем файлы из', files_directory)    
files_names = os.listdir(files_directory)    
print('В директории найдены файлы:', *files_names)    
    
headers_template = ['id', 'name', 'surname', 'age', 'height', 'weight', 'eyesight', 'education', 'english_language']    
    
colors = ['green', 'magenta', 'blue', 'yellow', 'cyan', 'red', 'light_blue', 'green', 'magenta']    
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
     

        # Создаем список для хранения отформатированных и проверенных данных
        data_to_sort = []
        out_condidat = []
        candidates_27_37 = []
        other_candidates = []

        for row in reader:
            formatted_data = []
            age = int(row[headings.index('age')])
            eyesight = float(row[headings.index('eyesight')])
            weight = int(row[headings.index('weight')])
            education = str(row[headings.index('education')])
            english_language = str(row[headings.index('english_language')])
            height = int(row[headings.index('height')])
            full_name = row[headings.index('name')] + ' ' + row[headings.index('surname')]
            
            if age >= 20 and age <= 59 and eyesight == 1.0 and weight >= 50 and weight <= 90:
                if education == 'Master' or education == 'PhD':
                    if english_language == 'true':
                        if height >= 150 and height <= 190:
                            for idx, header in enumerate(headers_template):
                                if header in headings:
                                    value = row[headings.index(header)] if headings.index(header) < len(row) else ''
                                    color = colors[idx]
                                    formatted_data.append(colored(f'{header}: {value}', color))
                            data_to_sort.append((full_name, formatted_data))
                            # Разделение кандидатов по возрасту
                            if 27 <= age <= 37:
                                candidates_27_37.append((full_name, formatted_data))
                            else:
                                other_candidates.append((full_name, formatted_data))

        candidates_27_37_sorted = sorted(candidates_27_37)
        other_candidates_sorted = sorted(other_candidates)

        print("Кандидаты с возрастом от 27 до 37 лет:")
        for name, data in candidates_27_37_sorted:
            print(name, *data, sep=' ')

        print("\nКандидаты не входящие в группу 27-37 лет:")
        for name, data in other_candidates_sorted:
            print(name, *data, sep=' ')


        # Сортировка данных по полному имени перед выводом
        sorted_data = []
        
        for name, data in sorted_data:   
            print(name, *data, sep='#')
        with open(('result.scv'), 'w', encoding='UTF-8') as file:
            writer = csv.writer(file, delimiter='#')
            writer.writerows(data_to_sort) 
    



        #сохранить файл: with open(('result.scv'), mode='w', encoding='utf-8') as file:
        #    writer = csv.writer(file, delimiter='#')
        #    writer.writerows(formatted_data)
        # какой элемент ряда к какому заголовку относится
        # меняю порядок в соответствии с шаблоном заголовков
        # добавляем упорядоченный ряд в копилку
