'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
HiBlu
By Mavericks

Objective: Program ini dibuat untuk mengambil data dari postgres, 
kemudian mengkonversikan file berbentuk csv menjadi JSON
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

# Import libraries yang dibutuhkan
import datetime as dt
import pandas as pd
import psycopg2 as db
import json
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

# Mengambil data dari PostgreSQL
def queryPostgresql():
    '''
    Mengambil data dari tabel hiblu_faq di PostgreSQL dan menyimpannya ke file CSV.

    Fungsi ini membuat koneksi ke database PostgreSQL menggunakan psycopg2,
    mengeksekusi query untuk mengambil semua data dari tabel public.hiblu_faq,
    dan menyimpannya ke file CSV dengan nama FAQ_cleaned.csv.
    '''
    conn_string = "dbname='airflow' host='postgres' user='airflow' password='airflow' port='5432'"
    conn = db.connect(conn_string)
    df = pd.read_sql("SELECT * FROM public.hiblu_faq", conn)
    df.to_csv('/opt/airflow/dags/FAQ_cleaned.csv')

# Konversi file CSV menjadi JSON
def convertCsvToJson():
    '''
    Mengonversi file CSV yang berisi data FAQ menjadi format JSON.

    Fungsi ini membaca data dari file CSV FAQ_cleaned.csv, kemudian mengonversi setiap
    baris menjadi objek JSON dengan format yang sesuai untuk chatbot (ChatGPT). Hasilnya disimpan
    ke dalam file JSON dengan nama FAQ.json.
    '''
    df = pd.read_csv('/opt/airflow/dags/FAQ_cleaned.csv')

    # Mendefinisikan pesan oleh sistem
    system_message = {"role": "system", "content": "Hi! HiBlu siap menjawab pertanyaanmu!"}

    # List kosong untuk menampung objek JSON
    json_data = []

    for index, row in df.iterrows():
        # Membuat array pesan untuk pertanyaan dan jawaban
        messages = [
            system_message,
            {"role": "user", "content": row['Question']},
            {"role": "assistant", "content": row['Answer']}
        ]
        # Memunculkan objek JSON ke dalam list
        json_data.append({"messages": messages})

    # Mengonversi daftar objek JSON ke string JSON dengan setiap objek di baris baru
    json_output = "\n".join(json.dumps(obj) for obj in json_data)

    # Save output JSON ke file
    output_path = '/opt/airflow/dags/FAQ.json'
    with open(output_path, 'w') as f:
        f.write(json_output)

# Mendefinisikan default_arg untuk DAG
default_args = {
    'owner': 'Mavericks',
    'start_date': dt.datetime(2024, 7, 3, 12, 0, 0),
}

# Mendefinisikan DAG
with DAG('HIBLU',
         default_args=default_args,
         schedule_interval='0 6 * * *',  # Run daily at 6:00 UTC
         catchup=False,
         concurrency=1,  # Ensure only one instance of the DAG runs at a time
         max_active_runs=1
         ) as dag:

    # Task - Mengambil data dari PostgreSQL
    getData = PythonOperator(
        task_id='QueryPostgreSQL',
        python_callable=queryPostgresql,
    )

    # Task - Konversi file CSV menjadi JSON
    convertCsvToJsonTask = PythonOperator(
        task_id='ConvertCsvToJson',
        python_callable=convertCsvToJson,
    )

# Mendefinisikan alur kerja DAG
getData >> convertCsvToJsonTask
