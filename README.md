# agriculture
<h2>Приложение для учёта сельскохозяйственных земель написанное на DRF</h2>

<b>Для развертывания проекта используется docker-compose.yml

В качестве базы данных используется образ с базой данных PostgreSQL</b>

Создаем файл .env с переменными:

<ul>
  <li>DEBUG</li>
  <li>SECRET_KEY</li>
  <li>ALLOWED_HOSTS</li>

  <li>SQL_ENGINE</li>
  <li>SQL_DATABASE</li>
  <li>SQL_USER</li>
  <li>SQL_PASSWORD</li>
  <li>SQL_HOST</li>
  <li>SQL_PORT</li>
  <li>DATABASE</li>
</ul>

И выполняем команду: 

<b>docker-compose -f   docker-compose.yml up -d --build</b>

Создаем базу данных в PostgreSQL и подключаем её к контейнеру(в настройках контейнера указан порт 5433:5432)

Далее выполняем миграции и пользуемся функционалом проекта

Регистрация пользователей и связывание их с моделью Фермеров происходит через админ панель

Для аутентификации используется Django Session-based Auth 
