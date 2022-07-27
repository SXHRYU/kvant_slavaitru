# Тестовое задание ФГУП "НИИ Квант"

## Установка

- Перейдите в папку, в которую хотите скачать файлы.
- Введите в командную строку (PowerShell, bash, zsh) следующее::
`git clone https://github.com/SXHRYU/Tetrika_slavaitru.git`
- Установите [Python](https://www.python.org/downloads/).
- Установите зависимости, введя в командную строку:
`pip install -r .\requirements.txt`
- Можно работать с файлами.

## Команды

После установки зависимостей, необходимо в командной строке прописать следующее:
- `python manage.py makemigrations`
- `python manage.py migrate`

Чтобы сразу вызвать метод **choose()** на случайно сгенерированные операции запустите файл `launch.py`
Этот файл запустит несколько операций в следующем порядке:
- `python manage.py create_executors`, который создаёт 10 исполнителей;
- `python manage.py random_ops`, который генерирует 10 случайных операций;
- `python manage.py choose`, который вызывает метод **choose()** и даёт ответ на задачу.

## Контакты

**Спасибо за уделённое время! Если возникнут вопросы, мои контакты:**
telegram: @SXRu1
e-mail: slavaitru@gmail.com
