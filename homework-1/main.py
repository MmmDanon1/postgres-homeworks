"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv
import os

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="1234"
)
cur = conn.cursor()

"Заполнение таблицы orders"
with open(os.path.join(os.path.dirname(__file__), "north_data", "orders_data.csv"), newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        order_id = row["order_id"]
        customer_id = row['customer_id']
        employee_id = row['employee_id']
        order_date = row['order_date']
        ship_city = row['ship_city']
        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (order_id, customer_id, employee_id, order_date, ship_city))
        cur.execute("SELECT*FROM orders")
        conn.commit()
    rows = cur.fetchall()
    for row in rows:
        print(row)

"Заполнение таблицы customers"
with open(os.path.join(os.path.dirname(__file__), "north_data", "customers_data.csv"), newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        customer_id = row["customer_id"]
        company_name = row['company_name']
        contact_name = row['contact_name']
        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (customer_id, company_name, contact_name))
        cur.execute("SELECT*FROM customers")
        conn.commit()
    rows = cur.fetchall()
    for row in rows:
        print(row)

"Заполнение таблицы employees"
with open(os.path.join(os.path.dirname(__file__), "north_data", "employees_data.csv"), newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        employee_id = row["employee_id"]
        first_name = row['first_name']
        last_name = row['last_name']
        title = row['title']
        birth_date = row['birth_date']
        notes = row['notes']
        cur.execute("INSERT INTO mployeese VALUES (%s, %s, %s, %s, %s, %s)",
                    (employee_id, first_name, last_name, title, birth_date, notes))
        cur.execute("SELECT*FROM mployeese")
        conn.commit()
    rows = cur.fetchall()
    for row in rows:
        print(row)

cur.close()
conn.close()


