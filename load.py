import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'basedescrapping'
}

def create_table():
    try:
        mydb = mysql.connector.connect(**DB_CONFIG)
        mycursor = mydb.cursor()
        mycursor.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                title TEXT,
                description TEXT,
                location TEXT,
                link VARCHAR(255) PRIMARY KEY UNIQUE,
                date TEXT
            )
        ''')
        mydb.commit()
    except mysql.connector.Error as err:
        print(f"Error creando la tabla: {err}")
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()

def insert_job(job):
    try:
        mydb = mysql.connector.connect(**DB_CONFIG)
        mycursor = mydb.cursor()
        sql = '''
            INSERT INTO jobs (title, description, location, link, date)
            VALUES (%s, %s, %s, %s, %s)
        '''
        val = (job['title'], job['description'], job['location'], job['link'], job['date'])
        mycursor.execute(sql, val)
        mydb.commit()
    except mysql.connector.IntegrityError:
        print(f"Advertencia: La oferta con enlace '{job['link']}' ya existe en la base de datos.")
    except mysql.connector.Error as err:
        print(f"Error insertando datos: {err}")
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()

def load_jobs(transformed_jobs):
    create_table()
    for job in transformed_jobs:
        insert_job(job)
    print(f"Se guardaron {len(transformed_jobs)} ofertas en la base de datos.")

if __name__ == "__main__":

    sample_transformed_data = [
        {"title": "Python Developer", "description": "", "location": "Lima, Peru", "link": "link1", "date": "2025-05-29"},
        {"title": "Senior Python Engineer", "description": "", "location": "San Isidro, Lima", "link": "link2", "date": "2025-05-28"}
    ]
    load_jobs(sample_transformed_data)