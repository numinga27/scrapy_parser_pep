# Асинхронный парсер PEP
## Описание проекта
Проект содержит парсер документов PEP на базе фреймворка Scrapy

Парсер выводит собранную информацию в два файла .csv:
В первый файл выводится список всех PEP: номер, название и статус.
Второй файл содержит сводку по статусам PEP — сколько найдено документов в каждом статусе (статус, количество). В последней строке этого файла в колонке «Статус» стоит слово Total, а в колонке «Количество» — общее количество всех документов.
## Инструкция по развёртыванию проекта
клонировать проект на компьютер:
<blockquote>git clone https://github.com/foxygen-d/scrapy_parser_pep.git</blockquote>
создание виртуального окружения:
<blockquote>python3 -m venv venv</blockquote>
запуск виртуального окружения:
<blockquote>. venv/bin/activate</blockquote>
установить зависимости из файла:
<blockquote>requirements.txt pip install -r requirements.txt</blockquote>
запуск команды на старт проекта:
<blockquote>scrapy startproject pep_parse .</blockquote>
создание паука:
<blockquote>scrapy genspider pep peps.python.org</blockquote>
запуск паука:
<blockquote>scrapy crawl pep</blockquote>
запуск тестов:
<blockquote>pytest</blockquote>

## Автор 
Крылов Андрей тг @numinga92
