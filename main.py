import os
import time
# print('Текущяя директория :',os.getcwd())
# if os.path.exists('first'):
#     os.chdir('first')
# else:
#     os.mkdir('first')
#     os.chdir('first')
# print('Текущяя директория :',os.getcwd())
# # os.makedirs(r'second\third\fourth')
# print(os.listdir())
# for i in os.walk('.'):
#     print(i)
# os.chdir(r'F:\проекты для URBAN Universety\Project7.5')
# print('Текущяя директория :',os.getcwd())
# print(os.listdir())
# file = [f for f in os.listdir() if os.path.isfile(f)]
# dirs = [d for d in os.listdir() if os.path.isdir(d)]
# print(dirs)
# print(file)

print('Текущяя директория :', os.getcwd())

directory ='.'

print(os.listdir())
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root,file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},'
              f' Родительская директория: {parent_dir}')







