### Hexlet tests and linter status:
[![Actions Status](https://github.com/Sophia-Filimonova/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Sophia-Filimonova/python-project-50/actions)
[![.github/workflows/pyci.yml](https://github.com/Sophia-Filimonova/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/Sophia-Filimonova/python-project-50/actions/workflows/pyci.yml)
<a href="https://codeclimate.com/github/Sophia-Filimonova/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/3e561a75ae07b9d982c9/maintainability" /></a>
<a href="https://codeclimate.com/github/Sophia-Filimonova/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/3e561a75ae07b9d982c9/test_coverage" /></a>


Требования: python версии ^3.10, pip версии 22 и выше, пакетный менеджер poetry.

Склонируйте репозиторий проекта локально, из корневой директории проекта выполните установку пакета командой make install, выполните сборку проекта командой make build, установите пакет в систему командой make package-install.

Программа вычисляет разницу между двумя древовидными структурами данных:
- поддерживаются разные входные форматы файлов: json, yaml
- результат сравнения выводится в разных форматах: stylish (по умолчанию), plain и json

Сli-утилита принимает через командную строку два аргумента — пути до сравниваемых файлов, и опцию --format, отвечающую за выбор формата:

usage: gendiff [-h] [-f FORMAT] first_file second_file


Пакет также можно использавать как библиотеку, которая предоставляет модуль gendiff с функцией generate_diff():

from gendiff import generate_diff

diff = generate_diff(file_path1, file_path2, format_name)
print(diff)

Обязательные аргументы file_path1 и file_path2 являются путями к сравниваемым файлам, необязательный параметр format_name выбирает вид представления результата и может принимать значения: stylish (по умолчанию, возвращает строку), plain (возвращает строку - плоский текст) и json (вывод в структурированном формате json)


Аскинема - Сравнение плоских файлов (JSON):
<a href="https://asciinema.org/a/2OqYPzEuPewucKLATjMEHAo3T" target="_blank"><img src="https://asciinema.org/a/2OqYPzEuPewucKLATjMEHAo3T.svg" /></a>

Аскинема - Сравнение плоских файлов (YAML):
<a href="https://asciinema.org/a/c4ULkuM97vKUWGRJpwqFWNNYd" target="_blank"><img src="https://asciinema.org/a/c4ULkuM97vKUWGRJpwqFWNNYd.svg" /></a>

Аскинема - Рекурсивное сравнение (JSON и YAML):
<a href="https://asciinema.org/a/DzazLmOM3m4qJZJEDRH6ZnqZq" target="_blank"><img src="https://asciinema.org/a/DzazLmOM3m4qJZJEDRH6ZnqZq.svg" /></a>

Аскинема - Плоский формат:
<a href="https://asciinema.org/a/X1suVY4gI7vPSTe0tstg7mKhP" target="_blank"><img src="https://asciinema.org/a/X1suVY4gI7vPSTe0tstg7mKhP.svg" /></a>

Аскинема - Вывод в JSON:
<a href="https://asciinema.org/a/s7XlNF16TVEjNauRFP2sq0E5C" target="_blank"><img src="https://asciinema.org/a/s7XlNF16TVEjNauRFP2sq0E5C.svg" /></a>