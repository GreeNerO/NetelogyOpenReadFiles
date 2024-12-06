import os

def merge_files(input_folder, output_file):
    # Получаем список файлов в указанной папке
    files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
    
    # Словарь для хранения содержимого файлов и их количества строк
    file_data = {}
    
    for file in files:
        with open(os.path.join(input_folder, file), 'r', encoding='utf-8') as f:
            lines = f.readlines()
            file_data[file] = lines
    
    # Сортируем файлы по количеству строк
    sorted_files = sorted(file_data.items(), key=lambda x: len(x[1]))
    
# Записываем результат в итоговый файл
    with open(output_file, 'w', encoding='utf-8') as output:
        for file_name, lines in sorted_files:
            output.write(f"{file_name}\n")
            output.write(f"{len(lines)}\n")
            output.writelines(lines)
            output.write("\n")  # Добавляем пустую строку между файлами

# Пример использования:
input_folder = "./files_for_merge"  # Укажите путь к папке с исходными файлами
output_file = "./files_for_merge/result/result.txt"            # Имя итогового файла

merge_files(input_folder, output_file)
