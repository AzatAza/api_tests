![image](https://img.shields.io/badge/Python-3.9-blue)
# Тесты 
## Список тестов
Описание тестов находится внутри тест-кейсов

Public api:
* Валидные данные
* Невалидные API ключи
* Невалидные данные

Front api:
* Валидные данные
* Невалидные данные

Perfomance:
* Производительность для обоих методов

## Как установить

Требуется `python3.9`

`pip install -r requirements.txt`

## Как запускать

1. Через Pycharm:
    * ПКМ по файлу
    * `Run 'pytest in file ..'`
    

2. Из консоли
   
   Используется логгер в тестах

   * `pytest` - запустит все
   * `pytest -m p0` - запустит только смоук тесты
   * `pytest -m p3` - запустит только негативные тесты
   * `pytest -m backend` - запустит только тесты бэкенда
   * `pytest -m frontend` - запустит только тесты фронтэнда
