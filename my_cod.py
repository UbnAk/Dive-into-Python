import os
import logging
from collections import namedtuple
import argparse

logging.basicConfig(filename='file.log', encoding='UTF-8', level=logging.INFO)

FileSis = namedtuple('FileSis', ['name', 'extension', 'is_dir', 'p_dir'])

def get_dir_info(path):
    my_list = []

    for root, dirs, files in os.walk(path): # root: Путь к текущему каталогу , dirs: Список директорий в текущем каталоге ,files: Список файлов в текущей директории.
        parent_directory = os.path.basename(root) # возвращает последний компонент пути path, то есть название файла или каталога.

        for file_name in files: # бегаем по файлам
            is_dir = False
            name, extension = os.path.splitext(file_name) # разделил 'dz.py' на 'dz' и '.py'
            file_s = FileSis(name, extension, is_dir, parent_directory)# создаем экземпляр класса с помощью nametuple
            my_list.append(file_s) #добавляем в список

        for dir_name in dirs: # бегаем по дирректория
            is_dir = True
            file_s = FileSis(dir_name, '', is_dir, parent_directory) #экземпляр
            my_list.append(file_s)

    return my_list


def main():
    parser = argparse.ArgumentParser(description='Получение информации о директории.')
    parser.add_argument('path', nargs='?', type=str, help='Путь к директории')

    args = parser.parse_args()

    if args.path:
        path = args.path
    else:
        path = input('Введите путь к директории: ')

    res = get_dir_info(path)
    for item in res:
        logging.info(item)


if __name__ == '__main__':
    main()