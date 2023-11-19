import sqlite3
import random
from faker import Faker

fake = Faker('ru_RU')  # Используем Faker для генерации фиктивных данных на русском языке

# Создаем соединение с базой данных
conn = sqlite3.connect('школа.db')
cursor = conn.cursor()

# Создаем таблицу "Ученики"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ученики (
        id INTEGER PRIMARY KEY,
        имя TEXT,
        возраст INTEGER,
        класс INTEGER,
        средний_балл REAL
    )
''')

# Заполняем таблицу "Ученики" случайными данными
for _ in range(450):
    cursor.execute('''
        INSERT INTO Ученики (имя, возраст, класс, средний_балл)
        VALUES (?, ?, ?, ?)
    ''', (fake.name(), random.randint(15, 18), random.randint(9, 11), round(random.uniform(2, 5), 2)))

# Создаем таблицу "Учителя"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Учителя (
        id INTEGER PRIMARY KEY,
        имя TEXT,
        предмет TEXT,
        стаж INTEGER
    )
''')

# Заполняем таблицу "Учителя" случайными данными
for _ in range(10):
    cursor.execute('''
        INSERT INTO Учителя (имя, предмет, стаж)
        VALUES (?, ?, ?)
    ''', (fake.name(), fake.word(), random.randint(1, 30)))

# Создаем таблицу "Предметы"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Предметы (
        id INTEGER PRIMARY KEY,
        название TEXT
    )
''')

# Заполняем таблицу "Предметы" случайными данными
предметы = ['Математика', 'Русский язык', 'Физика', 'Химия', 'История', 'Биология', 'Литература']
for предмет in предметы:
    cursor.execute('''
        INSERT INTO Предметы (название)
        VALUES (?)
    ''', (предмет,))

# Создаем таблицу "Оценки"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Оценки (
        id INTEGER PRIMARY KEY,
        id_ученика INTEGER,
        id_предмета INTEGER,
        оценка INTEGER
    )
''')

# Заполняем таблицу "Оценки" случайными данными
for id_ученика in range(1, 450):
    for id_предмета in range(1, 8):
        cursor.execute('''
            INSERT INTO Оценки (id_ученика, id_предмета, оценка)
            VALUES (?, ?, ?)
        ''', (id_ученика, id_предмета, random.randint(2, 5)))

# Создаем таблицу "Проекты"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Проекты (
        id INTEGER PRIMARY KEY,
        название TEXT,
        описание TEXT,
        дата_начала TEXT,
        дата_окончания TEXT
    )
''')

# Заполняем таблицу "Проекты" случайными данными
for _ in range(5):
    cursor.execute('''
        INSERT INTO Проекты (название, описание, дата_начала, дата_окончания)
        VALUES (?, ?, ?, ?)
    ''', (fake.word(), fake.text(), fake.date(), fake.date()))

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()
