import sqlite3

def execute_sql_file(file_path, connection):
    with open(file_path, 'r') as file:
        sql_statements = file.read()

    cursor = connection.cursor()
    cursor.executescript(sql_statements)
    connection.commit()

def create_database(database_name, schema_file):
    connection = sqlite3.connect(database_name)
    execute_sql_file(schema_file, connection)
    connection.close()

def fill_reg(conn, cur):
    with open('data_reg.txt') as file:
        for line in file:
            records = line.strip().split(',')

            cur.execute("INSERT INTO object_registry (id, type, name, crid, crdate, erdate)\
                    VALUES (?, ?, ?, ?, ?, ?)", (records[0], records[1], records[2], records[3], records[4], records[5]))
        conn.commit()

def fill_type(conn, cur):
    with open('data_type.txt') as file:
        for line in file:
            records = line.strip().split(',')

            cur.execute("INSERT INTO enum_object_type (id, name)\
                    VALUES (?, ?)", (records[0], records[1]))
        conn.commit()

def print_all_data(cur):
    row = [str(data) for data in cur.execute("SELECT * FROM object_registry")]
    print('\n'.join(row))

def command_1(cur):
    command = "SELECT object_registry.ID, enum_object_type.NAME AS type_name, object_registry.name,\
               object_registry.crid, object_registry.crdate, object_registry.erdate\
               FROM object_registry JOIN enum_object_type\
               ON object_registry.TYPE = enum_object_type.ID WHERE erdate IS NOT NULL\
               AND erdate != '' ORDER BY crdate DESC LIMIT 10;"
    
    cur.execute(command)
    table = cur.fetchall()

    for i in table:
        print(i)

def command_2(cur):
    cur.execute("BEGIN TRANSACTION;")

    command = "UPDATE object_registry SET erdate = CURRENT_TIMESTAMP\
            WHERE crdate < '2020-01-01 00:00:00'"
    cur.execute(command)
    cur.execute("COMMIT;")

if __name__ == "__main__":
    # Vytvorenie databázi
    database_name = "db_example.db"
    schema_file = "schema.sql"
    create_database(database_name, schema_file)

    conn = sqlite3.connect('db_example.db')
    cur = conn.cursor()

    # Naplneniee DB testovacími datami
    fill_reg(conn, cur)
    fill_type(conn, cur)

    # Výpis stavu dát v DB na začiatku
    print()
    print('Toto je výpis základného stavu tabulky:')
    print_all_data(cur)
    print()

    # Výpis výstupu z prvej úlohy
    print('Toto je výstup z prvej úlohy:')
    command_1(cur)
    print()

    # Výpis výstupu z druhej úlohy
    command_2(cur)
    print('Toto je výstup z druhej úlohy:')
    print_all_data(cur)

    conn.close()