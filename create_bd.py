import sqlite3


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
    CREATE TABLE rooms (
        id INTEGER PRIMARY KEY,
        name TEXT
    );
    ''')

    cursor.execute('''
    CREATE TABLE equipment (
        id INTEGER PRIMARY KEY,
        room_id INTEGER,
        device_name TEXT,
        full_device_name TEXT,
        processor TEXT,
        ram TEXT,
        system_type TEXT,
        windows_edition TEXT,
        windows_version TEXT,
        installation_date TEXT,
        windows_build TEXT,
        windows_feature_experience TEXT,
        image_path TEXT,
        FOREIGN KEY (room_id) REFERENCES rooms (id)
    );
    ''')

    connection.commit()


def insert_example_data(connection):
    cursor = connection.cursor()

    # Добавляем пример аудитории
    cursor.execute("INSERT INTO rooms (name) VALUES ('Аудитория 411');")
    room_id = cursor.lastrowid

    # Добавляем пример оборудования
    cursor.execute("""
    INSERT INTO equipment (
        room_id, device_name, full_device_name, processor, ram, system_type, windows_edition, windows_version, installation_date, windows_build, windows_feature_experience, image_path
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, (
        room_id, '411-7', '411-7.localvib.ru', 'Intel(R) Core(TM) i5-3450 CPU @ 3.10GHz', '8,00 ГБ (доступно: 7,69 ГБ)',
        '64-разрядная операционная система, процессор x64', 'Windows 10 Pro', '21H2', '27.05.2022', '19044.2728',
        '120.2212.4190.0', 'images/1.jpg'
    ))

    connection.commit()


def main():
    connection = sqlite3.connect('equipment_database.db')
    create_tables(connection)
    insert_example_data(connection)
    connection.close()


if __name__ == '__main__':
    main()
