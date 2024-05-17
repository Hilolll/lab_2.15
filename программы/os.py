import os

folder_path = "C:/Users/HP-PC/PycharmProjects/lab2.15/prog/os"  # Путь к папке с файлами
file_extension = ".txt"  # Расширение файлов, которые мы ищем

# Получаем список файлов с указанным расширением в папке
files = [f for f in os.listdir(folder_path) if
         os.path.isfile(os.path.join(folder_path, f)) and f.endswith(file_extension)]

# Переименовываем каждый файл, добавляя префикс "change_name"
for file in files:
    file_path = os.path.join(folder_path, file)
    new_file_name = "change_name" + file
    new_file_path = os.path.join(folder_path, new_file_name)

    print(f"Old filename: {file} -> New filename: {new_file_name}")

    # Переименование файла
    os.rename(file_path, new_file_path)