# TechRooms

TechRooms - это приложение на Python с использованием PyQt5 для отображения информации об аудиториях и техническом оборудовании из базы данных SQLite.

![Example.PNG](for%20readme%2Fimages%2FExample.PNG)  

## Установка

1. Убедитесь, что у вас установлен Python 3.6 или выше.


Для этого выполните команду:  

```bash
python --version
```  

2. Клонируйте репозиторий проекта:

```bash
git clone https://github.com/Pavel7811/TechRooms.git
```

3. Создайте и активируйте виртуальное окружение:

```bash
cd TechRooms
python -m venv venv
venv\Scripts\activate
```


4. Установите необходимые зависимости:

```bash
pip install -r requirements.txt
```

5. Создайте базу данных SQLite с помощью скрипта `create_bd.py`:

```bash
python create_bd.py
```


## Запуск приложения

Чтобы запустить приложение, выполните следующую команду:

```bash
python main.py
```

Приложение будет отображать список аудиторий и оборудования, хранящихся в базе данных SQLite. Выберите аудиторию, чтобы отобразить информацию об оборудовании и изображение.
