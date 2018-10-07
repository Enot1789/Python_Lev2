## Задание 1:

# s = "сокет"
# s1 = "декоратор"
# print(s.encode('utf-8'))
# encodeds = s.encode('utf-8')
# print(encodeds.decode('utf-8'))


##Задание 2: Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

# s = "\u0063\u006C\u0061\u0073\u0073"
# print(s)



## Задение 3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
# s2 = "attribute, класс, функция, type"
# print(s2.encode('utf-8'))

## Задание 4: Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).

# s = "разработка, администрирование, protocol, standard"
# print(s.encode('utf-8'))
# encodeds = s.encode('utf-8')
# print(encodeds.decode('utf-8'))


## Задание 5:Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.

# import subprocess
#
# args = ['ping', 'yandex.ru']
#
# subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
#
# for line in subproc_ping.stdout:
#     line = line.decode('cp866')
#     print(line)


## Задание 6:Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
## Примечание - не работает установк модуля chardet, Вы не могли бы уточнить почему так?

# import chardet

# filename = "test_file.txt"
# with open(filename, 'rb') as f:
#     res = chardet.detect(f.read())
# with open(filename, 'r', encoding=res['encoding']) as f:
#     print(f.read().encode('utf-8').decode('utf-8'))





# print(chr(97))

# print(ord('Z'))