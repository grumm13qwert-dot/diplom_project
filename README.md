# Интернет-магазин на Django


Пользователь может:

* зарегистрироваться и войти в аккаунт
* просматривать товары по категориям
* искать товары
* добавлять товары в корзину
* добавлять товары в избранное
* оставлять отзывы

---

##  Как запустить проект

### 1. Клонировать репозиторий


git clone https://github.com/grumm13qwert-dot/diplom_project.git
cd diplom_project


---

### 2. Создать виртуальное окружение


python -m venv venv
venv\Scripts\activate


---

### 3. Установить библиотеки


pip install -r requirements.txt


---

### 4. Применить миграции


python manage.py makemigrations
python manage.py migrate


---

### 5. Создать администратора


python manage.py createsuperuser


---

### 6. Запустить сервер


python manage.py runserver


---

### 7. Открыть сайт

Главная страница:

http://127.0.0.1:8000/

Админка:


http://127.0.0.1:8000/admin/


---

## Структура проекта

core/        - настройки проекта
products/    - товары и категории
users/       - регистрация и вход
cart/        - корзина
favorites/   - избранное
reviews/     - отзывы
templates/   - HTML шаблоны
media/       - изображения товаров


