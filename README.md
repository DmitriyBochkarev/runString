# runString
# Проект доступен на сайте https://random10208.pythonanywhere.com
# Запуск проекта на локальном сервере с помощью docker-compose:
## Создайте папку проекта, куда будете копировать репозиторий
## Откройте командную строку в этой папке
## Выполните следующие команды:
## Создаем локальный репозиторий:
```
git init
```
## Подключаем локальный репозиторий к удаленному:
```
git remote add origin  https://github.com/DmitriyBochkarev/runString.git
```
## Скачиваем удаленный репозиторий в локальный:
```
git pull https://github.com/DmitriyBochkarev/runString.git
```
## Переходим в папку mysite
```
cd mysite
```
## Создаем образ 
```
docker-compose build
```
## Запускаем контейнеры
```
docker-compose up
```
## Открываем браузер, пишем путь: "(ваш ip адрес):8000"

## Для настройки https создайте сертификат lets encrypt (потребуется установить certbot)
```
certbot certonly --standalone -d ваш-домен.ru
```

## Копируем сертификаты в папку ssl
cp /etc/letsencrypt/live/ваш-домен.ru/fullchain.pem .
cp /etc/letsencrypt/live/ваш-домен.ru/privkey.pem .

## Отредактируйте файл nginx.conf

