import json

import psycopg2

from config import config


def main():
    script_file = 'fill_db.sql'
    json_file = 'suppliers.json'
    db_name = 'my_new_db'

    params = config()
    conn = None

    create_database(params, db_name)
    print(f"БД {db_name} успешно создана")

    params.update({'dbname': db_name})
    try:
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                execute_sql_script(cur, script_file)
                print(f"БД {db_name} успешно заполнена")

                create_suppliers_table(cur)
                print("Таблица suppliers успешно создана")

                suppliers = get_suppliers_data(json_file)
                insert_suppliers_data(cur, suppliers)
                print("Данные в suppliers успешно добавлены")

                add_foreign_keys(cur)
                print(f"FOREIGN KEY успешно добавлены")

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def create_database(params, db_name) -> None:
    """Создает новую базу данных."""

    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE {db_name}")
    cur.execute(f"CREATE DATABASE {db_name}")

    conn.close()


def execute_sql_script(cur, script_file) -> None:
    """Выполняет скрипт из файла для заполнения БД данными."""

    with open(script_file, "r") as f:
        cur.execute(f.read())


def create_suppliers_table(cur) -> None:
    """Создает таблицу suppliers."""

    cur.execute("""
                CREATE TABLE suppliers (
                    company_name TEXT,
                    contact TEXT,
                    address TEXT,
                    phone TEXT,
                    fax TEXT,
                    homepage TEXT,
                    products TEXT
                                )
            """)


def get_suppliers_data(json_file: str) -> list[dict]:
    """Извлекает данные о поставщиках из JSON-файла и возвращает список словарей с соответствующей информацией."""

    with open(json_file) as json_file:
        suppliers = json.load(json_file)
        return suppliers



def insert_suppliers_data(cur, suppliers: list[dict]) -> None:
    """Добавляет данные из suppliers в таблицу suppliers."""

    for row in suppliers:
        company_name = row["company_name"]
        contact = row['contact']
        address = row['address']
        phone = row['phone']
        fax = row['fax']
        homepage = row['homepage']
        products = ' ,'.join(row['products'])
        cur.execute("INSERT INTO suppliers VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (company_name, contact, address, phone, fax, homepage, products))


def add_foreign_keys(cur) -> None:
    """Добавляет foreign key со ссылкой на supplier_id в таблицу products."""

    cur.execute('ALTER TABLE suppliers ADD COLUMN supplier_id serial;'
                'ALTER TABLE suppliers ADD CONSTRAINT fk_suppliers_supplier_id FOREIGN KEY (supplier_id) REFERENCES products (product_id)'
                )

if __name__ == '__main__':
    main()
