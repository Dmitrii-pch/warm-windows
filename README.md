# WarmWindows

Сайт компании WarmWindows — производителя тёплых окон с электроподогревом.

## Технологии
- Python 3.9
- Django 6.0.1
- SQLite

## Установка

1. Клонируй репозиторий:
```
git clone https://github.com/Dmitrii-pch/warm-windows.git
```

2. Установи зависимости:
```
pip install -r requirements.txt
```

3. Создай файл `.env` в корне проекта:
```
SECRET_KEY=твой_секретный_ключ
EMAIL_HOST_PASSWORD=пароль_от_почты
```

4. Примени миграции:
```
python manage.py migrate
```

5. Создай суперпользователя:
```
python manage.py createsuperuser
```

6. Запусти сервер:
```
python manage.py runserver
```

## Страницы
- Главная `/`
- Продукция `/products/`
- Технология `/technology/`
- Проекты `/projects/`
- Отзывы `/reviews/`
- FAQ `/faq/`
- Контакты `/contacts/`
- Политика конфиденциальности `/privacy/`