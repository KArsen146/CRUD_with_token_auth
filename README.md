# CRUD for Users with token authentication

## Установка и запуск проекта(для MacOs)

1. Склонируйте репозиторий и перейдите в папку с проектом:
```
git clone https://github.com/KArsen146/CRUD_with_token_auth
cd CRUD_with_token
```
2. Создайте и активируйте виртуальное окружение(venv):
```shell
virtualenv venv
source venv/bin/activate
```
3. Установите зависимоти (из файла requirements.txt):
```shell
pip install -r requirements.txt
```
4. Создайте и примените миграции
```shell
./manage.py makemigrations
./manage.py migrate
```
5. Создайте суперпользователя:
```shell
./manage.py createsuperuser
```
   Укажите Username, email address(опционально) и password
6. Запустите сервер:
```shell
./manage.py runserver "port number"
```
   Сервер запустится на localhost на порту port number
   Если вы не укажите port number, то по умолчанию сервер запустится на порту 8000

## Использование сервера
Для того чтобы Создавать/получать/обновлять/удалять пользователя, в header'e по ключу 'Authorization' необходимо указать 'Token <ваш токен>'
Пользовательская модель включает в себя следующие атрибуты:
+ username - Обязательное поле, имя пользователя, должно быть уникальным 
+ first_name - Имя 
+ last_name - Фамилия
+ email - Адрес электронной почты
+ is_staff - True, если пользователь является Staff, иначе False
+ is_active - True, если пользователь является активным
+ date_joined - Дата регистрации

### Получить токен
   POST ```/api-token-auth/```

   В Body необходимо указать логин и пароль пользователя, например:
   ```json
{
  "username": "newuser",
  "password": "newUserpassword123"
}
```
   В ответ вернется json такого вида:
```json
{
    "token": "<ваш токен>"
}
```
   
## Создать пользователя
POST ```/user/```

   В Body необходимо указать логин и пароль пользователя, например:
   ```json
{
  "username": "user1234",
  "password": "newUserpassword123"
}
```
   Также можно указать значения полей first_name, last_name, email, is_staff, is_active

## Получить список пользователей
GET ```/user/```

## Получить конкретного пользователя:
GET ```/user/<int:id>/```

## Изменить пользователя:
### Замена пользователя по id
PUT ```/user/<int:id>/``` - заменит пользователя с id на нового, который будет передан в Body запроса

Body запроса аналогичен Body запроса создания пользователя
### Изменение данных пользователя
PATCH ```/user/<int::id>/```
Body запроса должен содержать информацию о тех полях, значения которых Вы хотите изменить, например:
```json
{
  "first_name" : "Myname"
}
```

## Удалить пользователя:
DELETE ```/user/<int:id>/```


