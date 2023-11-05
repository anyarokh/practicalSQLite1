import sqlite3 as sl

conn = sl.connect('my_first_db.db')
cursor = conn.cursor()

# Дані в database:

# INSERT INTO product (name, description, price, category) VALUES
# ('Ноутбук Dell XPS 15', '15.6" 4K UHD екран, Intel Core i9, 32 ГБ RAM, 1 ТБ SSD', 2499.99, 'Ноутбуки'),
# ('Смартфон iPhone 13 Pro', '6.1" Super Retina XDR дисплей, A15 Bionic чіп, 128 ГБ', 1099.99, 'Смартфони'),
# ('LED Телевізор Sony Bravia 65" 4K', 'HDR, Android TV, Dolby Atmos', 799.99, 'Телевізори'),
# ('Фотокамера Canon EOS 5D Mark IV', '30.4 МП, 4K відео, Wi-Fi', 2499.99, 'Фотоапарати'),
# ('Ігрова консоль PlayStation 5', '4K Ultra HD Blu-ray, SSD, геймпад DualSense', 499.99, 'Ігрові консолі');

# INSERT INTO customer (name, surname, address, phone) VALUES
# ('Марія', 'Петрова', 'вул. Центральна, 123, Київ, Україна', '+380987654321'),
# ('Іван', 'Сидоренко', 'пр. Перемоги, 45, Львів, Україна', '+380987654322'),
# ('Ольга', 'Савченко', 'вул. Гагаріна, 56, Одеса, Україна', '+380987654323'),
# ('Андрій', 'Коваленко', 'вул. Пушкіна, 87, Харків, Україна', '+380987654324'),
# ('Віктор', 'Захаренко', 'вул. Шевченка, 12, Дніпро, Україна', '+380987654325');

# INSERT INTO orders (id_customer, creation_date, status) VALUES
# (1, '2023-11-05 10:00:00', 'Очікується'),
# (2, '2023-11-05 11:30:00', 'Відправлено'),
# (3, '2023-11-05 12:15:00', 'Очікується'),
# (4, '2023-11-05 13:45:00', 'Відправлено'),
# (5, '2023-11-05 14:30:00', 'Очікується');

# INSERT INTO order_details (id_order, id_product, quantity) VALUES
# (1, 1, 2),
# (1, 3, 1),
# (2, 2, 1),
# (3, 4, 2),
# (4, 5, 3);


# Запит 1
query1 = """
SELECT product.name, order_details.quantity
FROM order_details
INNER JOIN product ON product.id_product = order_details.id_product
INNER JOIN orders ON orders.id_order = order_details.id_order
WHERE orders.status = 'Очікується';
"""

# Виконання запиту 1
cursor.execute(query1)
result1 = cursor.fetchall()
print("Результат запиту 1:")
for row in result1:
    print(row)

# Запит 2
query2 = """
SELECT orders.id_order, orders.creation_date, orders.status
FROM orders
INNER JOIN customer ON customer.id_customer = orders.id_customer
WHERE customer.name = 'Ольга';
"""

# Виконання запиту 2
cursor.execute(query2)
result2 = cursor.fetchall()
print("\nРезультат запиту 2:")
for row in result2:
    print(row)

# Оновлення записів
update_query = """
UPDATE orders
SET status = 'Відправлено'
WHERE status = 'Очікується';
"""

cursor.execute(update_query)

# Запит 1
query1 = """
SELECT product.name, order_details.quantity
FROM order_details
INNER JOIN product ON product.id_product = order_details.id_product
INNER JOIN orders ON orders.id_order = order_details.id_order
WHERE orders.status = 'Очікується';
"""

# Виконання запиту 1
cursor.execute(query1)
result1 = cursor.fetchall()
print("Результат запиту 1:")
for row in result1:
    print(row)

# Запит 2
query2 = """
SELECT orders.id_order, orders.creation_date, orders.status
FROM orders
INNER JOIN customer ON customer.id_customer = orders.id_customer
WHERE customer.name = 'Ольга';
"""

# Виконання запиту 2
cursor.execute(query2)
result2 = cursor.fetchall()
print("\nРезультат запиту 2:")
for row in result2:
    print(row)

conn.commit()

conn.close()
