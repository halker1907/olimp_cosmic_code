import os    
import csv    
from termcolor import colored    
    
files_directory = r'C:\Users\IT\Desktop\Архив'    
print('читаем файлы из', files_directory)    
files_names = os.listdir(files_directory)    
print('В директории найдены файлы:', *files_names)    
    
headers_template = ['name', 'surname', 'age', 'height', 'weight', 'eyesight', 'education', 'english_language']    
    
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
     

        # Создаем список для хранения отформатированных и проверенных данных
        data_to_sort = []
    
        for row in reader:    
            formatted_data = []    
            age = int(row[headings.index('age')])    
            eyesight = float(row[headings.index('eyesight')])  
            weight = int(row[headings.index('weight')])  
            education = str(row[headings.index('education')])  
            english_language = str(row[headings.index('english_language')])  
            height = int(row[headings.index('height')]) 
            full_name = row[headings.index('name')] + ' ' + row[headings.index('surname')]  # Объединяем имя и фамилию
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

        # Сортировка данных по полному имени перед выводом
        sorted_data = sorted(data_to_sort, key=lambda x: x[0])

        for name, data in sorted_data:   
            print(name, *data, sep=' ')
      
    with open(('result.scv'), mode='w', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='#')
        for  header in formatted_data:
            writer.writerows(header + '\n') 
    



        #сохранить файл: with open(('result.scv'), mode='w', encoding='utf-8') as file:
        #    writer = csv.writer(file, delimiter='#')
        #    writer.writerows(formatted_data)
        # какой элемент ряда к какому заголовку относится
        # меняю порядок в соответствии с шаблоном заголовков
        # добавляем упорядоченный ряд в копилку
